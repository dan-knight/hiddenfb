from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from hiddenfb.utility.file_loader.csv import CSVFileLoader


def test__csv_loader__returns_valid_data():
    header: List[str] = ["ID", "test"]

    data: List[Dict[str, str]] = [
        {column: str(column_i + row_i) for column_i, column in enumerate(header)}
        for row_i in range(5)
    ]

    csv_data = "\n".join(
        [",".join(header), *[",".join(list(row.values())) for row in data]]
    )
    loader = CSVFileLoader()

    with patch("hiddenfb.utility.file_loader.open", mock_open(read_data=csv_data)):
        result: List[Dict[str, Any]] = loader.load(Path("test.csv"))

    assert result == data
