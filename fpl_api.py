import requests # type: ignore

def fetch_fpl_data():
    URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
    data = requests.get(URL).json()
    return data['elements'], data['teams']

def fetch_match_data(player_id):
    URL = f'https://fantasy.premierleague.com/api/element-summary/{player_id}/'
    data = requests.get(URL).json()
    return data