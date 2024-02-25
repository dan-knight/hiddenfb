from hiddenfb.domain.player import Player
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class PlayerMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> Player:
        return Player(player_id=event.player_id)
