from typing import Any, Dict
from hiddenfb.domain.match import Match
from hiddenfb.domain.moment.match import MatchMoment
from hiddenfb.test.domain.match import MatchTestUtility


class MatchMomentTestUtility:
    def __init__(
        self,
        match_utility: MatchTestUtility
    ):
        self._match_utility: MatchTestUtility = match_utility

    def create_match_moment(
        self,
        match: Match | None = None,
        frame: float = 1299.4
    ) -> MatchMoment:
        if match is None:
            match = self._match_utility.create_match()
        return MatchMoment(
            match=match,
            frame=frame
        )
    
    def assert_equal(self, a: MatchMoment, b: MatchMoment) -> None:
        assert self.to_test_dict(a) == self.to_test_dict(b)

    def to_test_dict(self, match_moment: MatchMoment) -> Dict[str, Any]:
        result: Dict[str, Any] = match_moment.__dict__
        if match_moment.match is not None:
            result["match"] = self._match_utility.to_test_dict(match_moment.match)
        
        return result
