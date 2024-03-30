import re

from hiddenfb.domain.player import Player
from hiddenfb.schemas.data.metrica.event import MetricaEvent
from hiddenfb.schemas.data.wyscout.event import WyscoutEvent


class PlayerMapper:
    def from_wyscout_event(self, event: WyscoutEvent) -> Player:
        return Player(player_id=event.player_id)

    def from_metrica_event(self, event: MetricaEvent) -> Player:
        return Player(player_id=self._parse_metrica_player_id(event.player_from))

    def _parse_metrica_player_id(self, player_name: str) -> int:
        number_matches: list[str] = re.findall(r"\d+", player_name)
        if len(number_matches) == 0:
            raise ValueError(f'No player ID found in "{player_name}"')
        return int(number_matches[0])
