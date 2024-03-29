from hiddenfb.domain.coordinate.pitch import PitchCoordinates
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition


class CoordinatesMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> PitchCoordinates:
        try:
            start_position: WyscoutEventPosition = event.positions[0]
        except IndexError:
            raise ValueError("No positions found in Wyscout event.")

        return PitchCoordinates(
            x=start_position.x,
            y=start_position.y,
        )

    def from_metrica_event(self, event: MetricaEvent) -> PitchCoordinates:
        start_x: float
        start_y: float
        if event.event_subtype == "KICK_OFF":
            start_x, start_y = 0.5, 0.5
        elif event.start_x is None or event.start_y is None:
            raise ValueError("Missing event coordinates")
        else:
            start_x, start_y = event.start_x, event.start_y

        return PitchCoordinates(
            x=start_x,
            y=start_y,
        )
