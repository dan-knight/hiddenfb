class Match:
    def __init__(self, match_id: int):
        self._match_id: int = match_id

    @property
    def match_id(self) -> int:
        return self._match_id
