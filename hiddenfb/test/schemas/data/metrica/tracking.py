from typing import Any, Dict

from hiddenfb.schemas.data.metrica.tracking import MetricaTracking
from hiddenfb.test.schemas.data.metrica import MetricaTestUtility


class MetricaTrackingTestUtility(MetricaTestUtility):
    def create_tracking(
        self,
        id: str = "Player1",
        period: int = 1,
        frame: int = 10,
        time: float = 20.2,
        x: float | None = 10.5,
        y: float | None = 50.2,
    ) -> MetricaTracking:
        return MetricaTracking(id=id, period=period, frame=frame, time=time, x=x, y=y)

    def to_json(self, tracking: MetricaTracking) -> Dict[str, Any]:
        return {
            "id": self._to_string(tracking.id),
            "period": self._to_string(tracking.period),
            "frame": self._to_string(tracking.frame),
            "time": self._to_string(tracking.time),
            "x": self._to_string(tracking.x, default=self._default_value),
            "y": self._to_string(tracking.y, default=self._default_value),
        }
