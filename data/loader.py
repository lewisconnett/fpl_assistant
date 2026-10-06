from data.FPLClient import FPLClient
from data.FPLDataService import FPLDataService
import logging, requests


def initialise_app() -> FPLDataService | None:
    try:
        client = FPLClient()
        raw_data = client.fetch_fpl_data()
        fpl_data = FPLDataService(raw_data)

        _ = fpl_data.players
        _ = fpl_data.teams

        return fpl_data
    except (requests.RequestException, ValueError) as e:
        logging.error(f"Failed to initialise app: {e}")
        return None
