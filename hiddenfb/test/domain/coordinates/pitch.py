from hiddenfb.domain.coordinate.pitch import PitchCoordinates
from hiddenfb.test.domain.coordinates import CoordinatesTestUtility


class PitchCoordinatesTestUtility(CoordinatesTestUtility):
    def create_coordinates(self, x: float = 1.4, y: float = 10.5) -> PitchCoordinates:
        return PitchCoordinates(x=x, y=y)
