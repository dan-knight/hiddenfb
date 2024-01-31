import json
from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from hiddenfb.utility.file_loader.json import JSONFileLoader


def test__json_loader__returns_valid_data():
    data: List[Dict[str, Any]] = [{"test": "data"}, {"test": "valid"}]

    loader = JSONFileLoader()

    with patch(
        "hiddenfb.utility.file_loader.open", mock_open(read_data=json.dumps(data))
    ):
        result: List[Dict[str, Any]] = loader.load(Path("test.json"))

    assert result == data
