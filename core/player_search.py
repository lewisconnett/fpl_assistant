from rapidfuzz import process, fuzz, utils
from config import FUZZY_MATCH_MIN_SCORE
from data.global_data import get_player_data
from data.loader import initialise_app
from core.captaincy_model import evaluate_captaincy
from data.fpl_api import fetch_match_data
import logging
import requests


def find_player_by_name(search_query: str) -> dict | None:
    players_data = get_player_data()
    players = [f"{player['first_name']} {player['second_name']}" for player in players_data]
    
    match = process.extractOne(
        search_query,
        players,
        scorer=fuzz.WRatio,
        processor=utils.default_process
    )

    if not match:
        return None
    
    matched_name, score, index = match
    
    if score < FUZZY_MATCH_MIN_SCORE:
        return None
    else:
        return players_data[index] 
    
def find_player_by_id(id: int) -> dict | None:
    try:
        players_data = get_player_data()
    except ValueError as e:
        print(f'Error: {e}. Attempting to initialise data...')
        initialise_app()
        try:
            players_data = get_player_data()
        except ValueError as e:
            print(f'Failed to initialise player data: {e}')
            return None
        
    for player in players_data:
        if player['id'] == id:
            return player

    return None

def get_captain_data(player: dict) -> dict | None:
    try:
        match_data = fetch_match_data(player['id'])
        position = player['element_type']
        availability = player['status']    
        chance_of_playing_next_round = player['chance_of_playing_next_round'] or 100
        result = evaluate_captaincy(match_data, position, availability, chance_of_playing_next_round)
        logging.info(f"Successfully evaluated captaincy for player ID {player['id']}")
        return result
        
    except requests.RequestException as e:
        logging.error(f'API Error: {e}')
        return None
    except ValueError as e:
        logging.error(f'Data error: {e}')
        return None
    except Exception as e:
        logging.error(f'Unexpected error loading data: {e}')
        return None