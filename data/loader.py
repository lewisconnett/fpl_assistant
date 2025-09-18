from data.fpl_api import fetch_fpl_data
from core.utils import map_team_ids

def initialise_app():
    
    try:
        players_data, team_data = fetch_fpl_data()
        teams = map_team_ids(team_data)
        print('Data loaded successfully!')
        return players_data, teams
    except Exception as e:
        print(f'Error loading data: {e}')
        return None, None