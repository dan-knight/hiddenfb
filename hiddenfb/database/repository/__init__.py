from hiddenfb.utility.file_loader import FileLoader


class Repository: ...


class FileRepository:
    def __init__(self, file_loader: FileLoader):
        self._loader: FileLoader = file_loader
