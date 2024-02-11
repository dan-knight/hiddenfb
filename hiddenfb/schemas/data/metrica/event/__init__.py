from dataclasses import dataclass


@dataclass(frozen=True)
class MetricaEvent:
    team: str
    event_type: str
    event_subtype: str | None
    period: int
    start_frame: int
    end_frame: int
    start_time: float
    end_time: float
    player_from: str
    player_to: str | None
    start_x: float | None
    start_y: float | None
    end_x: float | None
    end_y: float | None
