import pandas as pd
from config import POSITION_SCALE, RECENT_MATCHES_FOR_AVAILABILITY,  FORM_RECENT_MATCHES, FORM_SCORE_SCALE, AVAILABILITY_MULTIPLIERS, FULL_GAME_THRESHOLD, AVAILABILITY_WEIGHTINGS, FPL_FIXTURE_DIFFICULTY_SCALE, DEFAULT_TRIPLE_CAPTAIN_RECOMMENDATION, TRIPLE_CAPTAIN_RULES, CAPTAINCY_WEIGHTS, CAPTAIN_RATING_THRESHOLDS, POSITION_MULTIPLIERS, PURPLE_PATCH_THRESHOLD, PURPLE_PATCH_BONUS

def evaluate_captaincy(match_data: dict, position: str, availability_status: str, chance_of_playing_next_round: int) -> dict:
    if chance_of_playing_next_round == 0 or availability_status in ['i', 's', 'u']:
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
    
    position_factor =  POSITION_MULTIPLIERS.get(position, 1.0) * POSITION_SCALE
    
    captain_score = (
        form_score * CAPTAINCY_WEIGHTS['form'] +
        fixture_score * CAPTAINCY_WEIGHTS['fixture'] +
        availability_score * CAPTAINCY_WEIGHTS['availability'] +
        position_factor * CAPTAINCY_WEIGHTS['position']
    )
        
    return {
        'score': captain_score,
        'rating': get_captain_rating(captain_score),
        'triple_recommendation': get_triple_recommendation(captain_score, position)
    }

def calculate_form_score(match_history: pd.DataFrame) -> float:
    form = match_history['total_points'].tail(FORM_RECENT_MATCHES).mean()
    season_avg = match_history['total_points'].mean()
    
    if form > season_avg * PURPLE_PATCH_THRESHOLD:
        purple_patch_bonus = PURPLE_PATCH_BONUS
    else:
        purple_patch_bonus = 1.0
        
    return min((form * purple_patch_bonus) / FORM_SCORE_SCALE, 10)

def calculate_availability_score(match_history: pd.DataFrame, availability_status: str, chance_of_playing_next_round: int) -> float:
    recent_matches = match_history.tail(RECENT_MATCHES_FOR_AVAILABILITY)
    
    matches_played = (recent_matches['minutes'] > 0).sum()
    matches_played_rate = matches_played / len(recent_matches)
    
    full_matches = (recent_matches['minutes'] >= FULL_GAME_THRESHOLD).sum()
    full_matches_rate = full_matches / max(matches_played, 1)
    
    avg_minutes = recent_matches['minutes'].mean()
    minutes_score = min(avg_minutes / 90, 1.0)
    
    availability_multiplier = AVAILABILITY_MULTIPLIERS.get(availability_status, 1.0) * (chance_of_playing_next_round / 100)
        
    availability_score = (
        matches_played_rate * AVAILABILITY_WEIGHTINGS['start_rate'] +
        full_matches_rate * AVAILABILITY_WEIGHTINGS['full_games'] +
        minutes_score * AVAILABILITY_WEIGHTINGS['minutes']
    ) * availability_multiplier * 10
    
    return min(availability_score, 10)  

def calculate_fixture_difficulty(upcoming_fixtures: pd.DataFrame) -> float:
    return (FPL_FIXTURE_DIFFICULTY_SCALE - upcoming_fixtures['difficulty'].iloc[0]) * 2

def get_captain_rating(captain_score: float) -> str:
    for threshold, rating in CAPTAIN_RATING_THRESHOLDS.items():
        if captain_score >= threshold:
            return rating

def get_triple_recommendation(captain_score: float, position: str) -> str:
    for rule in TRIPLE_CAPTAIN_RULES:
        if captain_score >= rule['min_score'] and position in rule['position']:
            return rule['recommendation']
    
    return DEFAULT_TRIPLE_CAPTAIN_RECOMMENDATION