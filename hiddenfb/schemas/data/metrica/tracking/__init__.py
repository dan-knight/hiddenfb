from dataclasses import dataclass


@dataclass(frozen=True)
class MetricaTracking:
    id: str
    period: int
    frame: int
    time: float
    x: float | None
    y: float | None
