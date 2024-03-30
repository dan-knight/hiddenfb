from hiddenfb.domain.coordinate.pitch import PitchCoordinates
from hiddenfb.mappings.domain.coordinates import CoordinatesMapper
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition
from hiddenfb.test.domain.coordinates.pitch import PitchCoordinatesTestUtility
from hiddenfb.test.schemas.data.metrica.event import MetricaEventTestUtility
from hiddenfb.test.schemas.data.wyscout.event import WyscoutEventTestUtility


def test__coordinates_mapper__creates_from_wyscout_event():
    coordinate_utility = PitchCoordinatesTestUtility()
    x: int = 3
    y: int = 5
    coordinates: PitchCoordinates = coordinate_utility.create_coordinates(x=x, y=y)

    event_utility = WyscoutEventTestUtility()
    event: WyscoutEvent = event_utility.create_event(
        positions=[WyscoutEventPosition(x=x, y=y)]
    )

    mapper = CoordinatesMapper()
    result: PitchCoordinates = mapper.from_wyscout_event(event)

    coordinate_utility.assert_equal(result, coordinates)


def test__coordinates_mapper__creates_from_metrica_event():
    coordinate_utility = PitchCoordinatesTestUtility()
    coordinates: PitchCoordinates = coordinate_utility.create_coordinates()

    event_utility = MetricaEventTestUtility()
    event: MetricaEvent = event_utility.create_event(
        start_x=coordinates.x, start_y=coordinates.y
    )

    mapper = CoordinatesMapper()
    result: PitchCoordinates = mapper.from_metrica_event(event)

    coordinate_utility.assert_equal(result, coordinates)
