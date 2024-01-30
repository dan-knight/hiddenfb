from dataclasses import dataclass

from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.player import Player


@dataclass
class PlayerMoment:
    player: Player
    match_moment: MatchMoment
    action: PlayerAction
