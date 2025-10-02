from data.fpl_api import fetch_fpl_data
from core.utils import map_team_ids
from data.global_data import init_data
import requests
import logging

logger = logging.getLogger('fpl_tool.log')

def initialise_app() -> bool:
    try:
        players_data, team_data = fetch_fpl_data()
        teams = map_team_ids(team_data)
        init_data(players_data, teams)
        logging.info('Data loaded successfully')
        return True
    except requests.RequestException as e:
        logging.error(f'API error" {e}')
        return False
    except ValueError as e:
        logging.error(f'Data error: {e}')
        return False
    except Exception as e:
        logging.error(f'Unexpected error loading data: {e}')
        return False