import json
from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from hiddenfb.database.ETL.wyscout.file_loader.event import WyscoutEventLoader


def test__wyscout_event_loader__loads_valid_format():
    data: List[Dict[str, str | List[str] | List[Dict[str, str]]]] = [
        {
            "eventId": str(i + 1),
            "subEventName": "Simple pass",
            "tags": [{"id": str(1801)}],
            "playerId": str(i * 3),
            "positions": [{"y": str(14 + i), "x": str(29 - i)}],
            "matchId": str(150),
            "eventName": "Pass",
            "teamId": str(191),
            "matchPeriod": "1H",
            "eventSec": str(i + 0.988**i),
            "subEventId": str(71),
            "id": str(i * 100 + 10 + i**2),
        }
        for i in range(5)
    ]

    loader = WyscoutEventLoader()

    with patch(
        "hiddenfb.utility.file_loader.open", mock_open(read_data=json.dumps(data))
    ):
        result: List[Dict[str, Any]] = loader.load(Path("test.json"))

    assert result == data
