from dataclasses import dataclass

from hiddenfb.domain.coordinate import Coordinates
from hiddenfb.utility.exception.number import NegativeNumberError


@dataclass
class PitchCoordinates(Coordinates):
    def __post_init__(self):
        if self.x < 0:
            raise NegativeNumberError(self.x, "x")
        if self.y < 0:
            raise NegativeNumberError(self.y, "x")
