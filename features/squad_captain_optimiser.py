import pyinputplus as pyip
from ui.squad_captain_optimiser import show_menu, check_users_team, handle_wrong_team, display_best_captain_pick
from core.squad_captain_optimiser import get_team_info, get_squad_picks, get_squad_captaincy_ratings
from core.player_search import find_player_by_id
import logging

def run_captaincy_optimiser():
    show_menu()
    while True:
        team_id = pyip.inputNum("Enter your team's ID: ") # 1080106
        team_info = get_team_info(team_id)
        
        if not team_info:
            print(f'❌ Could not find team with ID {team_id}. Please try again.')
            continue
      
        check_users_team(team_info)    
        confirmed_team = pyip.inputYesNo('Is this the correct team? [Y/N]: ')
            
        if confirmed_team == 'yes':
            print("Great! We’ve confirmed your team - let’s continue.\n")
            
            gw = 6 # fetch this dynamically
            result = calculate_best_captain(team_id, gw)
                
            display_best_captain_pick(result)
            
            continue_choice = pyip.inputYesNo('\n Would you like to check another team? [Y/N]: ')
            if continue_choice == 'no':
                print('Thanks for using the captain optimiser! Good Luck! 🎯')
                break
                
        else:
            handle_wrong_team()
            

def calculate_best_captain(team_id: int, gw: int) -> dict:
    '''
    Calculate the best captain choice for a team in a given gameweek
    
    Args:
        team_id: The FPL team ID
        gw: the gameweek number
        
    Returns:
        dict: {
            'success': bool,
            'message': str,
            'data': dict or None
        }
    '''
    logging.info(f'Starting squad captain optimiser for team ID: {team_id}')
    
    # Step 1: Get squad picks
    
    squad_picks = get_squad_picks(team_id, gw)
    
    if not squad_picks:
        logging.warning(f'Could not retrieve squad picks for team {team_id}')
        return {
            'success': False,
            'message': f'Unable to load you squad for GW {gw}',
            'data': None
        }
        
    logging.info(f'Retrieved {len(squad_picks)} squad picks')
    
    # Step 2: Get player objects
    player_objects = []
    missing_players = []
    
    for pick in squad_picks:
        player = find_player_by_id(pick['element'])
        
        if player:
            player_objects.append(player)
        else:
            missing_players.append(pick['element'])
            logging.warning(f'Could not retrieve player with ID: {pick['element']}')
            
    if not player_objects:
        logging.error(f'No valid players for team {team_id}')
        return {
            'success': False,
            'message': 'Could not load any players from your squad. The player database may be outdated',
            'data': None
        }
        
    if missing_players:
        logging.warning(f'{len(missing_players)} could not loaded: {missing_players}')
        
    logging.info(f'Successfully loaded {len(player_objects)} players')
    
    # Step 3: Get captaincy ratings
    
    try:
        captaincy_scores = get_squad_captaincy_ratings(player_objects)
    except Exception as e:
        logging.error(f'Error calculating captaincy scores: {e}')
        return {
            'success': False,
            'message': 'There seems to be an error calculating the captaincy scores. Please try again.',
            'data': None
        }
    
    if not captaincy_scores:
        logging.warning('No captain scores were generated')
        return {
            'success': False,
            'message': 'Could not calculate captain scores. Captain data may be unavailable.',
            'data': None
        }
        
    valid_scores = {name: score for name, score in captaincy_scores.items() if score is not None}
 
    if not valid_scores:
        logging.warning('No valid captain scores where found')
        return {
            'success': False,
            'message': 'No captain data available for your players this gameweek.',
            'data': None
        }
        
    # Step 4: Find best captain and alternatives
    
    sorted_scores = sorted(captaincy_scores.items(), key=lambda x: x[1]['score'], reverse=True)       
    best_player, best_data = sorted_scores[0]
    best_score = best_data['score']
    
    logging.info(f'✓ Best captain: {best_player} (score: {best_score})')  
    
    return {
        'success': True,
        'message': f'Successfuly calculated best captain for GW {gw}',
        'data': {
            'player_name': best_player,
            'score': best_score,
            'alternatives': sorted_scores[:5]
        }
    }