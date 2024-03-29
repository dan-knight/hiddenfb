from dataclasses import dataclass
from enum import StrEnum


class MetricaEventType(StrEnum):
    SHOT = "SHOT"
    PASS = "PASS"
    SET_PIECE = "SET PIECE"
    BALL_LOST = "BALL LOST"
    RECOVERY = "RECOVERY"
    CHALLENGE = "CHALLENGE"
    BALL_OUT = "BALL OUT"
    FAULT = "FAULT RECEIVED"
    CARD = "CARD"


class MetricaShotEventSubtype(StrEnum):
    GOAL = "GOAL"
    MISSED = "OUT"
    SAVE = "SAVE"
    BLOCKED = "BLOCKED"
    HEADER = "HEAD"
    ON_TARGET = "ON TARGET"
    OFF_TARGET = "OFF TARGET"
    POST = "WOODWORK"


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
