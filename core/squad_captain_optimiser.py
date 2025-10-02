import pprint
from data.fpl_api import fetch_team_info, fetch_squad_picks
from core.player_search import get_captain_data
import logging
import requests

def get_team_info(team_id: int) -> dict:
    try:
        return fetch_team_info(team_id)    
    except Exception as e:
        print(f'Error getting team info for ID {team_id}: {e}')
        
def get_squad_picks(team_id: int, gw: int) -> dict | None:
    logging.info(f'Getting squad picks for team ID: {team_id}, GW: {gw}')
    try:
        squad_picks = fetch_squad_picks(team_id, gw)
        
        logging.info(f'Successfully got squad picks for team ID: {team_id}, GW: {gw}')
        return squad_picks['picks']
    
    except requests.ReadTimeout as e:
        logging.error(f'API Error: {e}')
        return None
    except ValueError as e:
        logging.error(f'Data error: {e}')
        return None
    except Exception as e:
        logging.error(f'Unexpected error loading data: {e}')
        return None
        
def get_squad_captaincy_ratings(players: list) -> dict:
    logging.info(f'Starting captaincy ratings for {len(players)} players')
    
    squad_captaincy_scores = {}
    
    for player in players:
        player_name = player['web_name']
        logging.info(f'Processing captaincy rating for {player_name}')
        captain_score = get_captain_data(player)
        
        if captain_score:
            squad_captaincy_scores[player_name] = captain_score
            logging.debug(f'✔️ player name: {captain_score}')
        else:
            # Find a way to gracefully handle none becuase of error
            pass
    
    logging.info(f'Completed and sorted captaincy ratings: {len(players)} processed')

    return squad_captaincy_scores