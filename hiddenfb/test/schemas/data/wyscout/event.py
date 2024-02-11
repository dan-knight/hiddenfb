from typing import Any, Dict, List

from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.position import WyscoutEventPosition
from hiddenfb.schemas.data.wyscout.event.tag import WyscoutEventTag
from hiddenfb.test.schemas.data.wyscout import WyscoutTestUtility


class WyscoutEventTestUtility(WyscoutTestUtility):
    def create_event(
        self,
        event_id: int = 1,
        player_id: int = 25,
        team_id: int = 14,
        match_id: int = 41,
        period: str = "1H",
        event_time: float = 125.98,
        event_type_id: int = 4,
        event_type_name: str = "Pass",
        sub_event_id: int | None = 2,
        sub_event_name: str | None = "Header",
        tags: List[WyscoutEventTag] | None = None,
        positions: List[WyscoutEventPosition] | None = None,
    ) -> WyscoutEvent:
        if tags is None:
            tags = [self.create_event_tag()]
        if positions is None:
            positions = [self.create_event_position(x=i, y=i * 14) for i in range(1, 3)]

        return WyscoutEvent(
            event_id=event_id,
            player_id=player_id,
            team_id=team_id,
            match_id=match_id,
            period=period,
            event_time=event_time,
            event_type_id=event_type_id,
            event_type_name=event_type_name,
            sub_event_id=sub_event_id,
            sub_event_name=sub_event_name,
            tags=tags,
            positions=positions,
        )

    def create_event_tag(self, tag_id: int = 10) -> WyscoutEventTag:
        return WyscoutEventTag(tag_id=tag_id)

    def create_event_position(self, x: int = 10, y: int = 24) -> WyscoutEventPosition:
        return WyscoutEventPosition(x=x, y=y)

    def to_json(self, event: WyscoutEvent) -> Dict[str, Any]:
        return {
            "id": self._to_string(event.event_id),
            "playerId": self._to_string(event.player_id),
            "teamId": self._to_string(event.team_id),
            "matchId": self._to_string(event.match_id),
            "matchPeriod": event.period,
            "eventSec": self._to_string(event.event_time),
            "eventId": self._to_string(event.event_type_id),
            "eventName": event.event_type_name,
            "subEventId": self._to_string(event.sub_event_id, default=""),
            "subEventName": self._to_string(event.sub_event_name, default=""),
            "tags": [self.tag_to_json(tag) for tag in event.tags],
            "positions": [
                self.position_to_json(position) for position in event.positions
            ],
        }

    def tag_to_json(self, tag: WyscoutEventTag) -> Dict[str, Any]:
        return {"id": self._to_string(tag.tag_id)}

    def position_to_json(self, position: WyscoutEventPosition) -> Dict[str, Any]:
        return {"x": self._to_string(position.x), "y": self._to_string(position.y)}
