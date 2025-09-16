from player_search import findPlayer
from fpl_api import fetch_fpl_data, fetch_match_data
from utils import map_team_ids
from player_stats import assess_captaincy_potential, format_player_stats, positions, availability_statuses

players_data, team_data = fetch_fpl_data()
teams = map_team_ids(team_data)

search_query = input('Enter player name: ').lower()

player = findPlayer(players_data, search_query)

if player:  
    team_info = teams[player['team']]
    match_data = fetch_match_data(player['id'])
    position = positions[player['element_type']]
    availability_status = availability_statuses[player['status']]
    chance_of_playing_next_round = player['chance_of_playing_next_round']
    captain_data = assess_captaincy_potential(match_data, position, availability_status, chance_of_playing_next_round)
    formatted_player_stats = format_player_stats(player, team_info, captain_data, match_data, availability_status)
    print(f"Player: {formatted_player_stats['first_name']} {formatted_player_stats['second_name']}")
    print(f"Team: {formatted_player_stats['team']}")
    print(f"Position: {formatted_player_stats['position']}")
    print(f"Status: {formatted_player_stats['status']['availability']}")
    print(f"Captain Score: {formatted_player_stats['captain_rating']['score']:.2f}")
    print(f"Captain Rating: {formatted_player_stats['captain_rating']['rating']}")
    print(f"Triple Captain Recommendation: {formatted_player_stats['captain_rating']['triple_recommendation']}")
    if 'reason' in formatted_player_stats['captain_rating']:
        print(f"Reason: {formatted_player_stats['captain_rating']['reason']}")
else:
    print("Player Not Found!")
    
