from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from hiddenfb.utility.file_loader import FileLoader

ModelType = TypeVar("ModelType")
StoreType = TypeVar("StoreType")


class Repository(Generic[ModelType, StoreType], ABC):
    @abstractmethod
    def _to_model(self, stored: StoreType) -> ModelType: ...

    @abstractmethod
    def _from_model(self, model: ModelType) -> StoreType: ...


class FileRepository(Repository[ModelType, StoreType]):
    def __init__(self, file_loader: FileLoader):
        self._loader: FileLoader = file_loader
