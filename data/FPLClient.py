import requests
from config import BOOTSTRAP_STATIC, ELEMENT_SUMMARY, ENTRY_INFO, SQUAD_PICKS


class FPLClient:
    def __init__(self):
        self.session = requests.Session()

    def _get(self, url: str) -> dict:
        """
        Sends an HTTP GET request to the specified FPL API URL.

        Args:
            url (str): The complete API endpoint URL to fetch data from.

        Returns:
            dict: The decoded JSON response payload from the API.

        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful
                status code (e.g., 404 Client Error, 500 Server Error).
            requests.exceptions.JSONDecodeError: If the API response cannot be parsed as valid JSON.
        """

        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def _validate_data(self, data: dict) -> dict:
        """
        Validates the structure and integrity of the fetched FPL data.

        Ensures that the parsed payload is both a dictionary structure and contains
        populated, non-empty data fields.

        Args:
            data (dict): The raw, parsed JSON data dictionary to validate.

        Returns:
            dict: The validated data dictionary if all checks pass.

        Raises:
            ValueError: If the data is not a dictionary format, or if the
                dictionary is completely empty.
        """
        if not isinstance(data, dict):
            raise ValueError("Invalid FPL data format: response is not a dictionary")

        if not data:
            raise ValueError("FPL Data is empty")

        return data

    def fetch_fpl_data(self) -> dict:
        """Fetches the master bootstrap-static FPL data dataset.

        Returns the main game configuration data, including a full list of all Premier League teams, players (elements), gameweek schedules, and chip details.
        """

        return self._validate_data(self._get(BOOTSTRAP_STATIC))

    def fetch_element_summary(self, player_id: int) -> dict:
        """Fetches detailed season history, fixtures, and stats for a single player."""

        return self._validate_data(
            self._get(ELEMENT_SUMMARY.format(player_id=player_id))
        )

    def fetch_manager_info(self, entry_id: int) -> dict:
        """Fetches profile details, overall rank, and total points for a specific FPL manager."""

        return self._validate_data(self._get(ENTRY_INFO.format(entry_id=entry_id)))

    def fetch_squad_picks(self, entry_id: int, gw: int) -> dict:
        """Fetches the 15-player lineup, captain choices, and chips active for a manager in a specific gameweek."""

        return self._validate_data(
            self._get(SQUAD_PICKS.format(entry_id=entry_id, gw=gw))
        )
