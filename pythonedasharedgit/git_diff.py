"""
pythonedasharedgit/git_diff.py

This file declares the GitDiff class.

Copyright (C) 2023-today rydnr's pythoneda-shared/git

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.value_object import attribute
from pythonedasharedgit.git_diff_failed import GitDiffFailed
import subprocess

class GitDiff:
    """
    Provides git diff operations.

    Class name: GitDiff

    Responsibilities:
        - Provides "git diff" operations.

    Collaborators:
        - pythonedasharedgit.git_diff_failed.GitDiffFailed: If the operation fails.
    """

    def __init__(self, folder: str):
        """
        Creates a new GitDiff instance for given folder.
        :param folder: The cloned repository.
        :type folder: str
        """
        super().__init__()
        self._folder = folder

    @property
    @attribute
    def folder(self) -> str:
        """
        Retrieves the folder of the cloned repository.
        :return: Such folder.
        :rtype: str
        """
        return self._folder

    def diff(self) -> str:
        """
        Retrieves the diff.
        :return: The diff if the operation succeeds.
        :rtype: str
        """
        result = None

        try:
            execution = subprocess.run(
                ["git", "-C", self.folder, "diff"],
                check=True,
                capture_output=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.folder,
            )
            result = execution.stdout
        except subprocess.CalledProcessError as err:
            logging.getLogger(__name__).error(err.stdout)
            logging.getLogger(__name__).error(err.stderr)
            raise GitDiffFailed(self.folder)

        return result
