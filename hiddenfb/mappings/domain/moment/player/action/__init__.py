from typing import Generator, Set

from hiddenfb.domain.moment.player.action import PlayerAction
from hiddenfb.domain.moment.player.action.shot import Shot, ShotResult
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.metrica.event.metadata import (
    MISSED_SHOT_SUBTYPES,
    MetricaShotEventSubtype,
)
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent
from hiddenfb.schemas.data.wyscout.event.metadata import (
    OFF_TARGET_SHOT_TAGS,
    ON_TARGET_SHOT_TAGS,
    POST_SHOT_TAGS,
    WyscoutEventID,
    WyscoutShotEventTag,
)


class PlayerActionMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> PlayerAction:
        tag_ids: Set[int] = set([tag.tag_id for tag in event.tags])

        if event.event_id == WyscoutEventID.SHOT:
            return Shot(result=self._parse_wyscout_shot_result(tag_ids))
        else:
            raise ValueError(f"Invalid event ID {event.event_id}.")

    def from_metrica_event(self, event: MetricaEvent) -> PlayerAction:
        if event.event_type == "SHOT":
            return Shot(result=self._parse_metrica_shot_result(event))
        else:
            raise ValueError(f"Invalid event type {event.event_type}.")

    def _parse_wyscout_shot_result(self, tags: Set[int]) -> ShotResult:
        shot_result: ShotResult

        def missed(event_tags: Set[int]) -> Generator[bool, None, None]:
            for tag in event_tags:
                yield tag in OFF_TARGET_SHOT_TAGS or tag in POST_SHOT_TAGS

        def saved(event_tags: Set[int]) -> Generator[bool, None, None]:
            for tag in event_tags:
                yield tag in ON_TARGET_SHOT_TAGS

        if WyscoutShotEventTag.GOAL in tags:
            shot_result = ShotResult.GOAL
        elif any(missed(tags)):
            shot_result = ShotResult.MISS
        elif any(saved(tags)):
            shot_result = ShotResult.SAVE
        else:
            raise ValueError(
                f'Invalid shot tags ({", ".join([str(tag) for tag in tags])}).'
            )

        return shot_result

    def _parse_metrica_shot_result(self, event: MetricaEvent) -> ShotResult:
        if event.event_subtype is None:
            raise ValueError("No shot subtype found.")

        shot_result: ShotResult
        if MetricaShotEventSubtype.GOAL in event.event_subtype:
            shot_result = ShotResult.GOAL
        elif MetricaShotEventSubtype.SAVE in event.event_subtype:
            shot_result = ShotResult.SAVE
        elif event.event_subtype in MISSED_SHOT_SUBTYPES:
            shot_result = ShotResult.MISS
        else:
            raise ValueError(f'Invalid shot subtype "{event.event_subtype}"')

        return shot_result
