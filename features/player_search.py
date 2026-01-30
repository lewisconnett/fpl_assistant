from core.player_search import find_player_by_name
from config import POSITIONS, AVAILABILITY_STATUSES
from core.player_search import get_captain_data
from data.global_data import FPLData
from ui.player_search_ui import show_player
import logging
import pyinputplus as pyip

def run_player_search(fpl_data: FPLData):
    '''Main entry point for player search'''
    logging.info('Running player search feature')
    while True:
        player_name = pyip.inputStr('Enter player name: ').lower()
        
        result = search_player(player_name, fpl_data)
        
        show_player(result)
        
        continue_choice = pyip.inputYesNo('Would you like to lookup another player? [Y/N]: ')
        if continue_choice == 'no':
            logging.info('Player search feature has closed. Redirecting user back to main menu')
            break
            
            
def search_player(player_name: str, fpl_data: FPLData) -> dict:
    '''Get player and captain data and packages it'''
    
    player = find_player_by_name(player_name, fpl_data)
        
    if not player:
        return {
            'success': False,
            'message': 'Unfortunately we could not find that player',
            'data': None
        }
    
    captain_data = get_captain_data(player)
    teams = fpl_data.teams
    
    # Step 3: Package data up
    
    try:
        player_profile = package_player_data(player, captain_data, teams)
    except Exception as e:
        logging.error(f'Error packaging player data: {e}')
        return {
            'success': False,
            'message': f'For some reason we could not create the player profile for {player.get('web_name', 'Unknown')}',
            'data': None
        }
    
    return {
        'success': True,
        'message': f"{player.get('web_name', 'Unknown')}'s player profile was successfully created.",
        'data': player_profile
    }

def package_player_data(player: dict, captain_data: dict, teams: dict) -> dict:
    logging.info(f'Packaging data for player ID: {player.get('id')}')
    
    profile = {
        'first_name': player['first_name'],
        'second_name': player['second_name'],
        'position': POSITIONS.get(player['element_type']),
        'team':  teams[player['team_code']]['name'],
        'status': AVAILABILITY_STATUSES.get(player['status']),
        'chance_of_playing_next_round': player['chance_of_playing_next_round'] if player['chance_of_playing_next_round'] is not None else 100,
        'captain_data': captain_data
    }
    
    logging.info(f'Successfully created player profile for player ID: {player['id']}')
    
    return profile