from typing import Generator, List, Set

from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.moment.player.action.shot import Shot, ShotResult
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent

SHOT_EVENT_ID: int = 10
GOAL_TAG = 100
MISSED_SHOT_TAGS: List[int] = list(range(1210, 1223 + 1))


class PlayerActionMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> PlayerAction:
        tag_ids: Set[int] = set([tag.tag_id for tag in event.tags])

        if event.event_id == SHOT_EVENT_ID:
            return Shot(result=self._shot_result(tag_ids))
        else:
            raise ValueError(f"Invalid event ID {event.event_id}.")

    def _shot_result(self, tags: Set[int]) -> ShotResult:
        shot_result: ShotResult

        miss_tags: Set[int] = set(MISSED_SHOT_TAGS)

        def missed(event_tags: Set[int]) -> Generator[bool, None, None]:
            for tag in event_tags:
                yield tag in miss_tags

        if GOAL_TAG in tags:
            shot_result = ShotResult.GOAL
        elif any(missed(tags)):
            shot_result = ShotResult.MISS
        else:
            shot_result = ShotResult.SAVE

        return shot_result
