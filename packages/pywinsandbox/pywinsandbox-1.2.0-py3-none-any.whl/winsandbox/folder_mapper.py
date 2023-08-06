import sys
import pathlib


class FolderMapper:
    """
    Generic Folder Mapper. Enables to map a folder to the new sandbox.
    """

    def __init__(self, folder_path, read_only=True):
        self._folder_path = pathlib.Path(folder_path)
        self._read_only = read_only

    def path(self):
        return self._folder_path

    def read_only(self):
        return self._read_only


class PythonMapper:
    """
    Maps the current Python installation to the new sandbox.
    """

    def path(self):
        return pathlib.Path(sys.executable).parent

    def read_only(self):
        return True
