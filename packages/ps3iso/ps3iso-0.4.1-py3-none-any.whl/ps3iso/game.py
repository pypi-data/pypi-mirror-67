from __future__ import annotations
import io
import os
import re
import glob
import subprocess
from pathlib import Path
from collections import Counter
from typing import Iterator, Union, List

from .sfo import SfoFile
from .sfo.errors import SfoParseError


class Game(object):
    """
    Class representing a set of files making up a Playstation 3 game
    An existing ``.iso`` file must be passed, files with any extension matching the base name
    will be found and included in all operations

    :param Path or str iso_path: Path to an existing .iso file
    """

    def __init__(self, iso_path):

        self.iso = Path(iso_path).resolve()
        self.sfo = self.extract_sfo(self.iso)
        self.files = {self.iso, *self.iso.parent.glob(glob.escape(self.iso.stem) + '.*')}

    @property
    def exists(self):
        return self.iso.exists()

    @classmethod
    def extract_sfo(cls, iso_path: Union[str, Path]) -> SfoFile:
        """
        Read the PARAM.SFO data from an ``.iso`` file

        .. seealso:: :meth:`.SfoFile.parse`

        :param iso_path: Path to the .iso file to read
        """
        iso_path = Path(iso_path)
        if not iso_path.exists():
            return SfoFile()
        cmd = ['isoinfo', '-i', str(iso_path), '-f']
        proc = subprocess.run(cmd, capture_output=True)
        proc.check_returncode()
        valid_paths = [b'/PS3_GAME/PARAM.SFO;1', b'/PSP_GAME/PARAM.SFO']
        path = next(filter(lambda x: x in valid_paths, proc.stdout.split()), False)
        assert path, "PARAM.SFO not found."
        cmd = ['isoinfo', '-i', str(iso_path), '-x', path]
        proc = subprocess.run(cmd, capture_output=True)
        proc.check_returncode()
        try:
            with io.BytesIO(proc.stdout) as f:
                return SfoFile.parse(f)
        except SfoParseError as ex:
            ex.args = ('Error while extracting SFO from %s: %s' % (iso_path, str(ex)),)
            raise

    def format_file(self, f: Union[str, Path], fmt: str, fill='') -> Path:
        """
        Return a new path for an input file, formatted according to the SFO data and format string.
        The existing file extension will be preserved.

        .. seealso:: :meth:`.SfoFile.format`

        :param f: Path to an existing file
        :param fmt: Formatting string to use for new file name
        :param fill: String to use for replacing invalid characters
        """
        f = Path(f)
        name = self.sfo.format(fmt)
        name = re.sub(r'[\\/*?:<>"|%]', fill, name)
        return (f.parent / name).with_suffix(f.suffix.lower())

    def print_info(self, fmt=None) -> None:
        r"""
        Print information about the current game set.
        Accepts a custom output formatting string with SFO parameter variable expansion support

        In addition to the variables described by :meth:`.SfoFile.format`,
        the following will be also expanded:

        ========  =========
        Variable  Parameter
        ========  =========
        %p        Full path of the existing file
        %f        File name of the existing file
        \\n       Newline character
        \\t       Tab character
        ========  =========


        .. seealso::
            :meth:`.SfoFile.format`

        :param str fmt: Formatting string to use for output
        """
        if fmt is not None:
            for f in self.files:
                print(self.sfo.format(fmt)
                      .replace('\\n', '\n')
                      .replace('\\t', '\t')
                      .replace('%f', f.name)
                      .replace('%p', str(f)))
        else:
            width = max(len(str(k)) for k, v in self.sfo)
            print(f'\n{self.iso}')
            print('\n'.join(f'\t{k.ljust(width)}: {v}' for k, v in self.sfo))

    def __repr__(self):
        return f'<{self.iso}|+{max(0, len(self.files) - 1)}>'

    @classmethod
    def search(cls, path: Union[str, Path]) -> Iterator[Game]:
        """
        Search for ``.iso`` files in the given path. Non-recursive and case-insensitive

        :param: Path to search
        """
        path = Path(path)
        if path.resolve().is_dir():
            for fpath in path.glob(r'*.[Ii][Ss][Oo]'):
                yield cls(fpath)
        else:
            yield cls(path)

    @staticmethod
    def rename_all(games: List[Game], fmt: str) -> int:
        """
        Rename all files for the given games according to the formatting string

        .. seealso:: :meth:`.SfoFile.format`

        :param games: List of games to rename
        :param fmt: Formatting string to use as file name template
        """
        # Create a list of (src, dst) tuples
        targets = set((f, game.format_file(f, fmt)) for game in games for f in game.files)
        # Remove duplicates
        counter = Counter(t[1] for t in targets)
        duplicates = set(t for t in targets if counter[t[1]] != 1)
        targets -= duplicates

        def maxwidth(_targets):
            return max(len(str(t[0])) for t in _targets)

        if targets:
            width = maxwidth(targets)
            for src, dst in sorted(targets, key=lambda x: x[0]):
                print(f'{str(src).ljust(width)} -> {dst}')
                src.rename(dst)
        else:
            print('No rename targets found.')

        if duplicates:
            print('\nCowardly refusing to rename files where duplicates would be overwritten:')
            width = maxwidth(duplicates)
            for src, dst in sorted(duplicates, key=lambda x: x[1]):
                print(f'\t{str(src).ljust(width)} -> {dst}')

        return len(targets)
