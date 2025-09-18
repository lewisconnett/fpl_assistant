import requests # type: ignore
from config import BOOTSTRAP_STATIC, ELEMENT_SUMMARY

def fetch_fpl_data():
    data = requests.get(BOOTSTRAP_STATIC).json()
    return data['elements'], data['teams']

def fetch_match_data(player_id):
    url = ELEMENT_SUMMARY.format(player_id=player_id)
    data = requests.get(url).json()
    return data