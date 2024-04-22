from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar

ModelType = TypeVar("ModelType")
PrimaryKeyType = TypeVar("PrimaryKeyType")


class EntityCache(Generic[ModelType, PrimaryKeyType], ABC):
    def __init__(self):
        self._cache: Dict[PrimaryKeyType, ModelType]

    def get_from_cache(self, x: PrimaryKeyType) -> ModelType | None:
        return self._cache.get(x)

    def add_to_cache(self, model: ModelType):
        primary_key: PrimaryKeyType = self._get_primary_key(model)
        self._cache[primary_key] = model

    @abstractmethod
    def _get_primary_key(self, model: ModelType) -> PrimaryKeyType:
        raise NotImplementedError()
