from typing import Type, TypeVar

from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.moment.player.action.shot import Shot, ShotResult

ActionType = TypeVar("ActionType", bound=PlayerAction)


class PlayerActionTestUtility:
    def create_player_action(
        self, action_type: Type[ActionType] = Shot
    ) -> PlayerAction:
        if action_type == Shot:
            return Shot(result=ShotResult.GOAL)
        else:
            raise ValueError(f"Invalid player action type {action_type}")
