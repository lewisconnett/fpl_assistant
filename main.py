from player_search import findPlayer
from fpl_api import fetch_fpl_data, fetch_match_data
from utils import map_team_ids
from player_stats import assess_captaincy_potential, format_player_stats

players_data, team_data = fetch_fpl_data()
teams = map_team_ids(team_data)

search_query = input('Enter player name: ').lower()

player = findPlayer(players_data, search_query)

if player:  
    team_info = teams[player['team']]
    match_data = fetch_match_data(player['id'])
    captain_data = assess_captaincy_potential(match_data)
    formatted_player_stats = format_player_stats(player, team_info, captain_data, match_data)
    print(formatted_player_stats)
else:
    print("Player Not Found!")
    
