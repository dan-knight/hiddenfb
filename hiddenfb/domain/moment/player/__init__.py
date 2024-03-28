from dataclasses import dataclass
from typing import Generic, TypeVar

from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.player import Player

ActionType = TypeVar("ActionType", bound=PlayerAction | None)


@dataclass
class PlayerMoment(Generic[ActionType]):
    player: Player
    match_moment: MatchMoment
    action: ActionType
