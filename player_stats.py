import pandas as pd

positions = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}

def format_player_stats(player: dict, team: dict, captain_data: dict, match_data: dict) -> dict:
    return {
        'id': player['id'],
        'first_name': player['first_name'], 
        'last_name': player['second_name'],
        'team': team['name'],
        'position': positions[player['element_type']],
        'photo': player['photo'],
        'captain_rating': captain_data,
        'next_fixture': match_data['fixtures'][0]
    }
    
    
def assess_captaincy_potential(match_data: dict) -> dict:
    history_df = pd.DataFrame(match_data['history'])
    fixtures_df = pd.DataFrame(match_data['fixtures'])
    
    form = history_df['total_points'].tail(5).mean()
    avg_mins = history_df['minutes'].tail(5).mean()
    fixture_difficulty = fixtures_df['difficulty'].iloc[0]
    points_per_game = history_df['total_points'].mean()
    
    form_score = min(form / 1.5, 10)
    minutes_score = min(avg_mins / 9, 10)
    fixture_score = (5 - fixture_difficulty) * 2
    ppg_score = min(points_per_game, 10)
    
    captain_score = (
        form_score * 0.5 +
        fixture_score * 0.3 +
        ppg_score * 0.2 +
        minutes_score * 0.1    
    )
    
    if captain_score >= 8:
        rating = "Gold"
    elif captain_score >= 5:
        rating = "Silver"
    else:
        rating = "Bronze"
        
    return {
        'score': captain_score,
        'rating': rating
    }


    