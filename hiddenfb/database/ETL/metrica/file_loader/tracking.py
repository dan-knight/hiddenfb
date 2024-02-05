from typing import Any, Dict, Iterator, List
from hiddenfb.utility.file_loader.csv import WideCSVFileLoader


class MetricaTrackingLoader(WideCSVFileLoader):
    def _parse_header(self, reader: Iterator[Any]) -> List[str]:
        rows_to_skip: int = 2
        for _ in range(rows_to_skip):
            next(reader)
        
        return next(reader)

    def _parse_row(self, row: List[str], header: List[str]) -> List[Dict[str, Any]]:
        period: str = row[0]
        frame: str = row[1]
        time_seconds: str = row[2]

        return [
            {
                "id": header[i],
                "period": period,
                "frame": frame,
                "time": time_seconds,
                "x": row[i],
                "y": row[i + 1]
            } for i in range(3, len(row) - 1, 2)
        ]
    