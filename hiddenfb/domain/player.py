class Player:
    def __init__(self, player_id: int):
        self._player_id: int = player_id

    @property
    def player_id(self) -> int:
        return self._player_id
