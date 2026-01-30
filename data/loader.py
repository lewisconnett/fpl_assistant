from data.fpl_api import fetch_fpl_data
from data.global_data import FPLData
import logging, requests


def initialise_app() -> FPLData | None:
    try:
        raw_data = fetch_fpl_data()
        fpl_data = FPLData(raw_data)
        
        _ = fpl_data.players
        _ = fpl_data.teams

        return fpl_data
    except (requests.RequestException, ValueError) as e:
        logging.error(f"Failed to initialise app: {e}")
        return None
