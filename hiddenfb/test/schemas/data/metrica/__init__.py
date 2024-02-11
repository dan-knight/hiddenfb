from typing import Literal

from hiddenfb.test import TestUtility


class MetricaTestUtility(TestUtility):
    @property
    def _default_value(self) -> Literal["NaN"]:
        return "NaN"
