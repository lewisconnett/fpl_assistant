from rapidfuzz import process, fuzz, utils # type: ignore
from config import FUZZY_MATCH_MIN_SCORE

def findPlayer(players_data: list, search_query: str) -> dict | None:
    players = [f"{player['first_name']} {player['second_name']}" for player in players_data]
    min_score = FUZZY_MATCH_MIN_SCORE
    
    match = process.extractOne(
        search_query,
        players,
        scorer=fuzz.WRatio,
        processor=utils.default_process
    )

    if not match:
        return None
    
    matched_name, score, index = match
    
    if score < min_score:
        return None
    else:
        return players_data[index] 