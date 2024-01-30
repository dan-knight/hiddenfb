class Team:
    def __init__(self, team_id: int, primary_name: str):
        self._team_id: int = team_id
        self.primary_name: str = primary_name

    @property
    def team_id(self) -> int:
        return self._team_id
