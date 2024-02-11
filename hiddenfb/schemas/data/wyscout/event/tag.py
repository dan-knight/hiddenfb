from dataclasses import dataclass


@dataclass(frozen=True)
class WyscoutEventTag:
    tag_id: int
