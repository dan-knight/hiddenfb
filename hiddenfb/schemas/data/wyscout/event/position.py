from dataclasses import dataclass


@dataclass(frozen=True)
class WyscoutEventPosition:
    x: int
    y: int
