from abc import ABC, abstractmethod
from contextlib import contextmanager
from io import TextIOWrapper
from pathlib import Path
from typing import Any, Dict, Generator, List


class FileLoader(ABC):
    @abstractmethod
    def load(self, path: Path) -> List[Dict[str, Any]]: ...

    @contextmanager
    def _load_file(
        self, path: Path, file_type: str
    ) -> Generator[TextIOWrapper, Any, None]:
        path_file_type: str = path.suffix.strip(".")
        if path_file_type != file_type:
            raise ValueError(
                f"Expected file of type {file_type} (received {path_file_type})"
            )

        with open(path, "r") as f:
            yield f
