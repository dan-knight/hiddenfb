from typing import TypeVar
from hiddenfb.domain.moment.player import PlayerMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.player import Player
from hiddenfb.test.domain.player import PlayerTestUtility


ActionType = TypeVar("ActionType", bound=PlayerAction | None)


class PlayerMomentTestUtility:
    def create_player_moment(
        self,
        player: Player | None = None,
        action: ActionType = None
    ) -> PlayerMoment[ActionType]:
        player_utility = PlayerTestUtility()
        if player is None:
            player = player_utility.create_player()
        
        raise NotImplementedError()
