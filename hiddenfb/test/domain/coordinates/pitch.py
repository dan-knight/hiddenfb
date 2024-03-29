from typing import Any, Dict

from hiddenfb.domain.coordinate import Coordinates
from hiddenfb.domain.coordinate.pitch import PitchCoordinates
from hiddenfb.test.domain.coordinates import CoordinatesTestUtility


class PitchCoordinatesTestUtility(CoordinatesTestUtility):
    def create_coordinates(self, x: float = 1.4, y: float = 10.5) -> PitchCoordinates:
        return PitchCoordinates(x=x, y=y)

    def assert_equal(self, a: Coordinates, b: Coordinates):
        assert self.to_test_dict(a) == self.to_test_dict(b)

    def to_test_dict(self, x: Coordinates) -> Dict[str, Any]:
        return x.__dict__
