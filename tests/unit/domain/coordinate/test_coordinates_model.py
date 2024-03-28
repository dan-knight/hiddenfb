from hiddenfb.domain.coordinate import Coordinates


def test__coordinates__are_equal_with_same_values():
    x: float = 10.5
    y: float = 9.1

    a = Coordinates(x=x, y=y)
    b = Coordinates(x=x, y=y)

    assert a == b
