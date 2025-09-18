from core.player_search import findPlayer
from config import POSITIONS, AVAILABILITY_STATUSES
from data.fpl_api import fetch_match_data
from core.captaincy_model import evaluate_captaincy
from ui.player_search_ui import show_player

def player_search(players_data: dict, teams: dict):
    while True:
        player_to_lookup = input('Enter player name: ').lower()
        
        try:
            player = findPlayer(players_data, player_to_lookup)
            
            if player:
                captain_data = get_captain_data(player)
                player_profile = package_player_data(player, captain_data, teams)
            
                show_player(player_profile)
                
        except Exception as e:
            print(f'Error finding player: {e}')
            

def package_player_data(player: dict, captain_data: dict, teams: dict) -> dict:
    return {
        'first_name': player['first_name'],
        'second_name': player['second_name'],
        'position': POSITIONS.get(player['element_type']),
        'team':  teams[player['team']]['name'],
        'status': AVAILABILITY_STATUSES.get(player['status']),
        'chance_of_playing_next_round': player['chance_of_playing_next_round'] or 100,
        'captain_data': captain_data
    }
    
def get_captain_data(player: dict) -> dict:
    match_data = fetch_match_data(player['id'])
    position = player['element_type']
    availability = player['status']    
    chance_of_playing_next_round = player['chance_of_playing_next_round'] or 100

    return evaluate_captaincy(match_data, position, availability, chance_of_playing_next_round)