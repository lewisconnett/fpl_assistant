import requests
from config import BOOTSTRAP_STATIC, ELEMENT_SUMMARY, TEAM_INFO, SQUAD_PICKS


def fetch_fpl_data() -> dict:

    response = requests.get(BOOTSTRAP_STATIC)
    response.raise_for_status()
    return validate_fpl_data(response.json())


def validate_fpl_data(data: dict) -> dict:

    if not isinstance(data, dict):
        raise ValueError("Invalid FPL data format: response is not a dictionary")

    if not data:
        raise ValueError("FPL Data is empty")

    return data


def fetch_match_data(player_id: int) -> dict:

    response = requests.get(ELEMENT_SUMMARY.format(player_id=player_id))
    response.raise_for_status()

    return validate_match_info(response.json())


def validate_match_info(data: dict) -> dict:

    if not isinstance(data, dict):
        raise ValueError("Invalid match data format: response is not a dictionary")

    if not data:
        raise ValueError("Match data is empty")

    return data


def fetch_team_info(team_id: int) -> dict:

    response = requests.get(TEAM_INFO.format(team_id=team_id))
    response.raise_for_status()

    return validate_team_info(response.json())


def validate_team_info(data: dict) -> dict:

    if not isinstance(data, dict):
        raise ValueError("Invalid team data format: response is not a dictionary")

    if not data:
        raise ValueError("Team info is empty")

    return data


def fetch_squad_picks(team_id: int, gw: int):

    response = requests.get(SQUAD_PICKS.format(team_id=team_id, gw=gw))
    response.raise_for_status()

    return validate_squad_picks(response.json())


def validate_squad_picks(data: dict) -> dict:

    if not isinstance(data, dict):
        raise ValueError("Invalid squad data format: response is not a dictionary")

    if not data:
        raise ValueError("Squad picks is empty")

    return data
