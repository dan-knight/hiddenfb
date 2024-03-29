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


MISSED_SHOT_SUBTYPES = frozenset((
    MetricaShotEventSubtype.MISSED,
    MetricaShotEventSubtype.BLOCKED,
    MetricaShotEventSubtype.OFF_TARGET,
    MetricaShotEventSubtype.POST
))
