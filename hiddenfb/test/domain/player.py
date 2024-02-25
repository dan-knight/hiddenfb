from typing import Any, Dict
from hiddenfb.domain.player import Player


class PlayerTestUtility:
    def create_player(
        self,
        player_id: int = 10
    ) -> Player:
        return Player(
            player_id=player_id
        )
    
    def assert_equal(self, a: Player, b: Player) -> None:
        assert self._to_test_dict(a) == self._to_test_dict(b)
    
    def _to_test_dict(self, player: Player) -> Dict[str, Any]:
        return player.__dict__
