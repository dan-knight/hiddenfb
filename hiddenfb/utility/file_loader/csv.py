import csv
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Iterator, List

from hiddenfb.utility.file_loader import FileLoader
from hiddenfb.utility.list import flatten


class BaseCSVFileLoader(FileLoader, ABC):
    def load(self, path: Path) -> List[Dict[str, Any]]:
        with self._load_file(path, file_type="csv") as f:
            data = csv.reader(f)

            header_columns: List[str] = self._parse_header(data)

            return flatten(
                [self._parse_row(row, header=header_columns) for row in data]
            )

    def _parse_header(self, reader: Iterator[Any]) -> List[str]:
        return next(reader)

    @abstractmethod
    def _parse_row(
        self, row: List[str], header: List[str]
    ) -> Dict[str, Any] | List[Dict[str, Any]]: ...


class CSVFileLoader(BaseCSVFileLoader):
    def _parse_row(self, row: List[str], header: List[str]) -> Dict[str, Any]:
        return {header[i]: value for i, value in enumerate(row)}


class WideCSVFileLoader(BaseCSVFileLoader, ABC):
    @abstractmethod
    def _parse_row(self, row: List[str], header: List[str]) -> List[Dict[str, Any]]: ...
