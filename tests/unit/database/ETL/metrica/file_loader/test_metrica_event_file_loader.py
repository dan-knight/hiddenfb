from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from hiddenfb.database.ETL.metrica.file_loader.event import MetricaEventLoader


def test__metrica_tracking_loader__loads_valid_format():
    data: List[Dict[str, str]] = [
        {
            "Team": "Home",
            "Type": "RECOVERY",
            "Subtype": "INTERCEPTION",
            "Period": str(1),
            "Start Frame": str(11 + i),
            "Start Time [s]": str(0.9 + i),
            "End Frame": str(12 + i),
            "End Time [s]": str(0.96 + i),
            "From": f"Player{i + 1}",
            "To": f"Player{i + 2}",
            "Start X": str(30.4 + i),
            "Start Y": str(1.1 + i),
            "End X": str(22.9 + i),
            "End Y": str(17 + i),
        }
        for i in range(5)
    ]
    header: List[str] = list(data[0].keys())

    csv_data = "\n".join(
        [
            ",".join(header),
            *[
                ",".join([event[column_name] for column_name in header])
                for event in data
            ],
        ]
    )

    loader = MetricaEventLoader()

    with patch("hiddenfb.utility.file_loader.open", mock_open(read_data=csv_data)):
        result: List[Dict[str, Any]] = loader.load(Path("test.csv"))

    assert result == data
