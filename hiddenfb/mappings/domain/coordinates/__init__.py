from hiddenfb.domain.coordinate.pitch import PitchCoordinates
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
