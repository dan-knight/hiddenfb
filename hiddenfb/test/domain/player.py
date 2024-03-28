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
        assert self.to_test_dict(a) == self.to_test_dict(b)
    
    def to_test_dict(self, player: Player) -> Dict[str, Any]:
        return player.__dict__
