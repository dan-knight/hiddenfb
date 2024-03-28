from hiddenfb.domain.coordinate import Coordinates
from hiddenfb.test import TestUtility


class CoordinatesTestUtility(TestUtility):
    def create_coordinates(self, x: float = 1.4, y: float = 10.5) -> Coordinates:
        return Coordinates(x=x, y=y)
