import pandas as pd

positions = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}
availability_statuses = {"a": "Available", "d": "Doubtful", "i": "Injured", "s": "Suspended", "u": "Unavailable"}

def format_player_stats(player: dict, team: dict, captain_data: dict, match_data: dict, availability_status: str) -> dict:
    return {
        'id': player['id'],
        'first_name': player['first_name'], 
        'second_name': player['second_name'],
        'team': team['name'],
        'position': positions[player['element_type']],
        'photo': player['photo'],
        'status': {
            'availability': availability_status,
            'chance_of_playing_next_round': player['chance_of_playing_next_round']       
            },
        'captain_rating': captain_data,
        'next_fixture': match_data['fixtures'][0]
    }
    
def assess_captaincy_potential(match_data: dict, position: str, availability_status: str, chance_of_playing_next_round: int) -> dict:
    if chance_of_playing_next_round == 0 or availability_status in ['Injured', 'Suspended', 'Unavailable']:
        captain_score = 0.0
        return {
            'score': captain_score,
            'rating': get_captain_rating(captain_score),
            'triple_recommendation': get_triple_recommendation(captain_score, position),
            'reason': f'Player unavailable (status: {availability_status}, chance: {chance_of_playing_next_round}%)'
        }
    
    
    match_history_df = pd.DataFrame(match_data['history'])
    upcoming_fixtures_df = pd.DataFrame(match_data['fixtures'])
    
    form_score = calculate_form_score(match_history_df)
    availability_score = calculate_availability_score(match_history_df, availability_status, chance_of_playing_next_round)
    fixture_score = calculate_fixture_difficulty(upcoming_fixtures_df)
    
    position_multipliers = {
        'GK': 0.6,
        'DEF': 0.8,
        'MID': 1.0,
        'FWD': 1.4
    }
    
    position_factor =  position_multipliers.get(position, 1.0) * 5
    
    captain_score = (
        form_score * 0.40 +
        fixture_score * 0.30 +
        availability_score * 0.15 +
        position_factor * 0.15
    )
        
    return {
        'score': captain_score,
        'rating': get_captain_rating(captain_score),
        'triple_recommendation': get_triple_recommendation(captain_score, position)
    }

def calculate_form_score(match_history_df: pd.DataFrame) -> float:
    form = match_history_df['total_points'].tail(3).mean()
    season_avg = match_history_df['total_points'].mean()
    
    if form > season_avg * 1.4:
        purple_patch_bonus = 1.5
    else:
        purple_patch_bonus = 1.0
        
    return min((form * purple_patch_bonus) / 1.5, 10)

def calculate_availability_score(match_history_df: pd.DataFrame, availability_status: str, chance_of_playing_next_round: int) -> float:
    recent_games = match_history_df.tail(5)
    
    games_started = (recent_games['minutes'] > 0).sum()
    start_rate = games_started / len(recent_games)
    
    full_games = (recent_games['minutes'] >= 85).sum()
    full_games_rate = full_games / max(games_started, 1)
    
    avg_minutes = recent_games['minutes'].mean()
    minutes_score = min(avg_minutes / 90, 1.0)
    
    availability_multiplier = chance_of_playing_next_round / 100 if chance_of_playing_next_round is not None else 1.0
    if availability_status == 'Doubtful':
        availability_multiplier = min(availability_multiplier, 0.5)
    elif availability_status == 'Available':
        availability_multiplier = min(availability_multiplier, 1.0)
        
    availability_score = (
        start_rate * 0.4 +
        full_games_rate * 0.3 +
        minutes_score * 0.3
    ) * availability_multiplier * 10
    
    return min(availability_score, 10)  

def calculate_fixture_difficulty(upcoming_upcoming_fixtures_df: pd.DataFrame) -> float:
    return (5 - upcoming_upcoming_fixtures_df['difficulty'].iloc[0]) * 2

def get_captain_rating(captain_score: float) -> str:
    thresholds = {
        8.5: "Platinum",
        7.5: "Gold", 
        6.0: "Silver",
        4.0: "Bronze",
        0.0: "Avoid"
    }
    
    for threshold, rating in thresholds.items():
        if captain_score >= threshold:
            return rating
    
    return "Avoid"

def get_triple_recommendation(captain_score: float, position: str) -> str:
    if position in ['FWD', 'MID'] and captain_score >= 8.5:
        return 'Strong'
    elif position == 'FWD' and captain_score >= 7:
        return 'Consider'
    else:
        return 'Avoid'