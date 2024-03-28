import pytest
from hiddenfb.domain.coordinate.pitch import PitchCoordinates

from hiddenfb.utility.exception.number import NegativeNumberError


def test__pitch_coordinate__errors_with_negative_x():
    negative_x: float = -10.5

    with pytest.raises(NegativeNumberError, match=str(negative_x)):
        PitchCoordinates(x=negative_x, y=10)


def test__pitch_coordinate__errors_with_negative_y():
    negative_y: float = -10.5

    with pytest.raises(NegativeNumberError, match=str(negative_y)):
        PitchCoordinates(x=9, y=negative_y)
