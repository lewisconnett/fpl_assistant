from rapidfuzz import process, fuzz, utils
from config import FUZZY_MATCH_MIN_SCORE
from core.captaincy_model import evaluate_captaincy
import logging
from data.FPLDataService import FPLDataService


def find_player_by_name(search_query: str, players: dict) -> dict:

    searchable_player_names = [
        f"{player['first_name']} {player['second_name']}" for player in players
    ]

    match = process.extractOne(
        search_query, searchable_player_names, scorer=fuzz.WRatio, processor=utils.default_process
    )

    if not match:
        raise ValueError(f'No match was found for "{search_query}"')

    _, score, index = match

    if score < FUZZY_MATCH_MIN_SCORE:
        raise ValueError(
            f'Fuzzy match score below threshold for "{search_query}" ({score} < {FUZZY_MATCH_MIN_SCORE})'
        )
    else:
        player = players[index]

        logging.info(f'{player['web_name']} was found for "{search_query}"')
        return player


def find_player_by_id(id: int) -> dict | None:
    try:
        players_data = get_player_data()
    except ValueError as e:
        print(f'[find_player_by_id] failed to search for "{id}" because {e}')
        return None

    for player in players_data:
        if player["id"] == id:
            return player

    return None


def get_captain_data(player: dict) -> dict | None:
    try:
        match_data = fetch_match_data(player["id"])
        logging.info(f"Successfully got match data for player_id={player['id']}")
    except Exception as e:
        logging.error(
            f"[get_captain_data] could not evaluate captaincy for player_id={player['id']}: {e}"
        )
        return None

    position = player["element_type"]
    availability = player["status"]
    chance_of_playing_next_round = player["chance_of_playing_next_round"] or 100
    result = evaluate_captaincy(
        match_data, position, availability, chance_of_playing_next_round
    )
    logging.info(f"Successfully evaluated captaincy for player ID {player['id']}")

    return result
