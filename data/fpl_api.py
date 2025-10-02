import requests
from config import BOOTSTRAP_STATIC, ELEMENT_SUMMARY, TEAM_INFO, SQUAD_PICKS

def fetch_fpl_data() -> dict:
    try:
        response = requests.get(BOOTSTRAP_STATIC)
        response.raise_for_status()
        data = response.json()
        
        if not isinstance(data, dict):
            raise ValueError('Invalid FPL data: response is not a dictionary')
        if 'elements' not in data or 'teams' not in data:
            raise ValueError("Invalid FPL data: missing 'elements' or 'teams' keys")
        if not data['elements'] or not data['teams']:
            raise ValueError('Invalid FPL data: empty players or team list')
        
        return data['elements'], data['teams']
    except requests.RequestException as e:
        raise requests.RequestException(f'API request failed: {e}')
    except ValueError as e:
        raise ValueError(f'Data parsing error: {e}')
    except Exception as e:
        raise Exception(f'Unexpected error in fetch_fpl_data: {e}')
    
def fetch_match_data(player_id: int) -> dict:
    try:
        url = ELEMENT_SUMMARY.format(player_id=player_id)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if not isinstance(data, dict):
            raise ValueError(f'Invalid match data format: response is not a dictionary')
        if 'history' not in data or 'fixtures' not in data:
            raise ValueError(f"Invalid match data: missing 'history' or 'fixtures' keys")
        
        return data
    
    except requests.RequestException as e:
        raise requests.RequestException(f'API request failed: {e}')
    except ValueError as e:
        raise ValueError(f'Data parsing error: {e}')
    except Exception as e:
        raise Exception(f'Unexpected error in fetch_match_data: {e}')

def fetch_team_info(team_id: int) -> dict:
    try:
        url = TEAM_INFO.format(team_id=team_id)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            raise ValueError('Invalid team data format: response is not a dictionary')
    
        return data

    except requests.RequestException as e:
        raise requests.RequestException(f'API request failed: {e}')
    except ValueError as e:
        raise ValueError(f'Data parsing error: {e}')
    except Exception as e:
        raise Exception(f'Unexpected error in fetch_team_info: {e}')

def fetch_squad_picks(team_id: int, gw: int):
    try:
        url = SQUAD_PICKS.format(team_id=team_id, gw=gw)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if not isinstance(data, dict):
            raise ValueError('Invalid squad data format: response is not a dictionary')
        
        return data
    
    except requests.RequestException as e:
        raise requests.RequestException(f'API request failed: {e}')
    except ValueError as e:
        raise ValueError(f'Data parsing error: {e}')
    except Exception as e:
        raise Exception(f'Unexpected error in fetch_squad_picks: {e}')
        