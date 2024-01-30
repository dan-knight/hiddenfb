from enum import StrEnum, auto

from hiddenfb.domain.moment.player.action import PlayerAction


class ShotResult(StrEnum):
    GOAL = auto()
    MISS = auto()
    SAVE = auto()


class Shot(PlayerAction):
    def __init__(self, result: ShotResult):
        self.result: ShotResult = result
