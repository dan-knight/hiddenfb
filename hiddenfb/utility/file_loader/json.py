import json
from pathlib import Path
from typing import Any, Dict, List, cast

from hiddenfb.utility.file_loader import FileLoader


class JSONFileLoader(FileLoader):
    def load(self, path: Path) -> List[Dict[str, Any]]:
        with self._load_file(path, file_type="json") as f:
            data: Any = json.load(f)

        if isinstance(data, list):
            data = cast(List[Any], data)

            for x in data:
                if not isinstance(x, dict):
                    raise TypeError(
                        f"JSON data must be a list of objects (received item of type {type(x)})"
                    )
            data = cast(List[Dict[str, Any]], data)
        elif isinstance(data, dict):
            data = [cast(Dict[str, Any], data)]
        else:
            raise TypeError(
                f"JSON data must be a list of objects (received {type(data)})"
            )

        return data
