from dataclasses import dataclass

from hiddenfb.domain.match import Match


@dataclass(frozen=True)
class MatchMoment:
    match: Match | None
    frame: float
