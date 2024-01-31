from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

import pytest

from hiddenfb.utility.file_loader import FileLoader


class _MockFileLoader(FileLoader):
    def load(self, path: Path) -> List[Dict[str, Any]]:
        raise NotImplementedError()

    def test_load(self, path: Path, file_type: str):
        with self._load_file(path, file_type=file_type) as f:
            return f


@patch("hiddenfb.utility.file_loader.open", mock_open())
def test__file_loader__raises_error_with_incorrect_file_type():
    loader = _MockFileLoader()

    path = Path("test_files/test.txt")
    expected_file_type: str = "csv"

    with pytest.raises(ValueError):
        loader.test_load(path, file_type=expected_file_type)
