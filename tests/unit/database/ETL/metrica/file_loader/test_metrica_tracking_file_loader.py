from functools import reduce
from operator import concat
from pathlib import Path
from typing import Any, Dict, List, Tuple
from unittest.mock import mock_open, patch

# fmt: off
from hiddenfb.database.ETL.metrica.file_loader.tracking import \
    MetricaTrackingLoader

# fmt: on


def test__metrica_tracking_loader__loads_valid_format():
    player_ids: List[int] = [1, 2, 3, 5]

    source_header: List[str] = ["Period", "Frame", "Time [s]"]
    for player in player_ids:
        source_header.append(str(player))
        source_header.append("")

    period: str = str(1)
    frame: str = str(2)
    time_seconds: str = str(0.5)

    data: List[Dict[str, str]] = [
        {
            "period": period,
            "frame": frame,
            "time": time_seconds,
            "id": str(player_id),
            "x": str(10.5),
            "y": str(11.1),
        }
        for player_id in player_ids
    ]

    def _player_to_csv(player: Dict[str, str]) -> Tuple[str, str]:
        return player["x"], player["y"]

    extra_row: str = ",".join([""] * len(source_header))

    csv_data = "\n".join(
        [
            extra_row,
            extra_row,
            ",".join(source_header),
            ",".join(
                [
                    period,
                    frame,
                    time_seconds,
                    *list(reduce(concat, [_player_to_csv(player) for player in data])),
                ]
            ),
        ]
    )

    loader = MetricaTrackingLoader()

    with patch("hiddenfb.utility.file_loader.open", mock_open(read_data=csv_data)):
        result: List[Dict[str, Any]] = loader.load(Path("test.csv"))

    assert result == data
