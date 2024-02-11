from dataclasses import dataclass
from typing import List

from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag


@dataclass(frozen=True)
class WyscoutEvent:
    event_id: int
    player_id: int
    team_id: int
    match_id: int
    period: str
    event_time: float
    event_type_id: int
    event_type_name: str
    sub_event_id: int | None
    sub_event_name: str | None
    tags: List[WyscoutEventTag]
    positions: List[WyscoutEventPosition]
