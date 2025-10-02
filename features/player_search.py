from core.player_search import find_player_by_name
from config import POSITIONS, AVAILABILITY_STATUSES
from core.player_search import get_captain_data
from ui.player_search_ui import show_player
from data.global_data import get_team_data
import logging

logger = logging.getLogger('fpl_tool.log')

def player_search():
    while True:
        player_to_lookup = input('Enter player name: ').lower()
        try:
            player = find_player_by_name(player_to_lookup)
            
            if player:
                captain_data = get_captain_data(player)
                player_profile = package_player_data(player, captain_data)
            
                show_player(player_profile)
                
        except Exception as e:
            print(f'Error finding player: {e}')
            

def package_player_data(player: dict, captain_data: dict) -> dict:
    teams = get_team_data()
    return {
        'first_name': player['first_name'],
        'second_name': player['second_name'],
        'position': POSITIONS.get(player['element_type']),
        'team':  teams[player['team']]['name'],
        'status': AVAILABILITY_STATUSES.get(player['status']),
        'chance_of_playing_next_round': player['chance_of_playing_next_round'] or 100,
        'captain_data': captain_data
    }