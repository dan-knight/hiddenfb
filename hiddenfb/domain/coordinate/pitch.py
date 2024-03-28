from dataclasses import dataclass

from hiddenfb.domain.coordinate import Coordinate
from hiddenfb.utility.exception.number import NegativeNumberError


@dataclass
class PitchCoordinate(Coordinate):
    def __post_init__(self):
        if self.x < 0:
            raise NegativeNumberError(self.x, "x")
        if self.y < 0:
            raise NegativeNumberError(self.y, "x")
