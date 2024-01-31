import csv
from pathlib import Path
from typing import Any, Dict, Iterator, List

from hiddenfb.utility.file_loader import FileLoader


class CSVFileLoader(FileLoader):
    def load(self, path: Path) -> List[Dict[str, Any]]:
        with self._load_file(path, file_type="csv") as f:
            data = csv.reader(f)

        header_columns: List[str] = self._parse_header(data)
        return [self._parse_row(row, header=header_columns) for row in data]

    def _parse_header(self, reader: Iterator[Any]) -> List[str]:
        return next(reader)

    def _parse_row(self, row: List[str], header: List[str]) -> Dict[str, Any]:
        return {header[i]: value for i, value in enumerate(row)}
