from typing import Any, Dict
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.test.schemas.data.metrica import MetricaTestUtility


class MetricaEventTestUtility(MetricaTestUtility):
    def create_event(
        self,
        team: str = "Team",
        event_type: str = "Pass",
        event_subtype: str | None = "Header",
        period: int = 1,
        start_frame: int = 1,
        end_frame: int = 2,
        start_time: float = 1.5,
        end_time: float = 2.5,
        player_from: str = "Player1",
        player_to: str | None = "Player2",
        start_x: float | None = 10.5,
        start_y: float | None = 1.4,
        end_x: float | None = 11.6,
        end_y: float | None = 21.1
    ) -> MetricaEvent:
        return MetricaEvent(
            team=team,
            event_type=event_type,
            event_subtype=event_subtype,
            period=period,
            start_frame=start_frame,
            end_frame=end_frame,
            start_time=start_time,
            end_time=end_time,
            player_from=player_from,
            player_to=player_to,
            start_x=start_x,
            start_y=start_y,
            end_x=end_x,
            end_y=end_y
        )

    def to_json(self, event: MetricaEvent) -> Dict[str, Any]:
        return {
            "Team": event.team,
            "Type": event.event_type,
            "Subtype": self._to_string(event.event_subtype, default=""),
            "Period": self._to_string(event.period, default=self._default_value),
            "Start Frame": self._to_string(event.start_frame, default=self._default_value),
            "End Frame": self._to_string(event.end_frame, default=self._default_value),
            "Start Time [s]": self._to_string(event.start_time, default=self._default_value),
            "End Time [s]": self._to_string(event.end_time, default=self._default_value),
            "From": event.player_from,
            "To": self._to_string(event.player_to, default=""),
            "Start X": self._to_string(event.start_x, default=self._default_value),
            "Start Y": self._to_string(event.start_y, default=self._default_value),
            "End X": self._to_string(event.end_x, default=self._default_value),
            "End Y": self._to_string(event.end_y, default=self._default_value)
        }