from typing import FrozenSet

from zmq import IntEnum


class WyscoutEventID(IntEnum):
    SHOT = 10


class WyscoutShotEventTag(IntEnum):
    GOAL = 101
    OWN_GOAL = 102
    ON_TARGET_LOW_LEFT = 1205
    ON_TARGET_LOW_CENTER = 1201
    ON_TARGET_LOW_RIGHT = 1202
    ON_TARGET_CENTER_LEFT = 1204
    ON_TARGET_CENTER = 1203
    ON_TARGET_CENTER_RIGHT = 1206
    ON_TARGET_HIGH_LEFT = 1208
    ON_TARGET_HIGH_CENTER = 1207
    ON_TARGET_HIGH_RIGHT = 1209
    OFF_TARGET_LOW_LEFT = 1212
    OFF_TARGET_LOW_RIGHT = 1210
    OFF_TARGET_CENTER_LEFT = 1211
    OFF_TARGET_CENTER_RIGHT = 1213
    OFF_TARGET_HIGH_LEFT = 1215
    OFF_TARGET_HIGH_CENTER = 1214
    OFF_TARGET_HIGH_RIGHT = 1216
    POST_LOW_LEFT = 1219
    POST_LOW_RIGHT = 1217
    POST_CENTER_LEFT = 1218
    POST_CENTER_RIGHT = 1220
    POST_HIGH_LEFT = 1222
    POST_HIGH_CENTER = 1221
    POST_HIGH_RIGHT = 1223


GOAL_TAGS: FrozenSet[WyscoutShotEventTag] = frozenset(
    (WyscoutShotEventTag.GOAL, WyscoutShotEventTag.OWN_GOAL)
)

ON_TARGET_SHOT_TAGS: FrozenSet[WyscoutShotEventTag] = frozenset(
    (
        WyscoutShotEventTag.ON_TARGET_LOW_LEFT,
        WyscoutShotEventTag.ON_TARGET_LOW_CENTER,
        WyscoutShotEventTag.ON_TARGET_LOW_RIGHT,
        WyscoutShotEventTag.ON_TARGET_CENTER_LEFT,
        WyscoutShotEventTag.ON_TARGET_CENTER,
        WyscoutShotEventTag.ON_TARGET_CENTER_RIGHT,
        WyscoutShotEventTag.ON_TARGET_HIGH_LEFT,
        WyscoutShotEventTag.ON_TARGET_HIGH_CENTER,
        WyscoutShotEventTag.ON_TARGET_HIGH_RIGHT,
    )
)


OFF_TARGET_SHOT_TAGS: FrozenSet[WyscoutShotEventTag] = frozenset(
    (
        WyscoutShotEventTag.OFF_TARGET_LOW_LEFT,
        WyscoutShotEventTag.OFF_TARGET_LOW_RIGHT,
        WyscoutShotEventTag.OFF_TARGET_CENTER_LEFT,
        WyscoutShotEventTag.OFF_TARGET_CENTER_RIGHT,
        WyscoutShotEventTag.OFF_TARGET_HIGH_LEFT,
        WyscoutShotEventTag.OFF_TARGET_HIGH_CENTER,
        WyscoutShotEventTag.OFF_TARGET_HIGH_RIGHT,
    )
)


POST_SHOT_TAGS: FrozenSet[WyscoutShotEventTag] = frozenset(
    (
        WyscoutShotEventTag.POST_LOW_LEFT,
        WyscoutShotEventTag.POST_LOW_RIGHT,
        WyscoutShotEventTag.POST_CENTER_LEFT,
        WyscoutShotEventTag.POST_CENTER_RIGHT,
        WyscoutShotEventTag.POST_HIGH_LEFT,
        WyscoutShotEventTag.POST_HIGH_CENTER,
        WyscoutShotEventTag.POST_HIGH_RIGHT,
    )
)
