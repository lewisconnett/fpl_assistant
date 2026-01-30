class FPLData:
    def __init__(self, raw_data: dict):
        self._raw = raw_data
        self._players = None
        self._teams = None

    @property
    def players(self):
        """Returns list of all players"""

        # Early return if already cached
        if self._players is not None:
            return self._players

        if "elements" not in self._raw:
            raise ValueError("FPL data is missing required 'elements' key")

        if not self._raw["elements"]:
            raise ValueError("Players data is empty")

        return self._raw["elements"]

    @property
    def teams(self):
        """Returns list of all teams"""

        # Early return if already cached
        if self._teams is not None:
            return self._teams

        if "teams" not in self._raw:
            raise ValueError("FPL data is missing required 'teams' key")

        if not self._raw["teams"]:
            raise ValueError("Teams data is empty")

        return self._raw["teams"]
