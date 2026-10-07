from config import AVAILABILITY_STATUSES, POSITIONS


def prepare_player_profile(player: dict, team: dict) -> dict:

    return {
        "name": (
            f'{player.get("first_name")} {player.get("second_name")}'
            if player.get("first_name") and player.get("second_name")
            else (player.get("web_name") or "Unknown")
        ),
        "position": POSITIONS.get(player.get("element_type")) or "Unknown",
        "team": team.get("name") or team.get("short_name") or "Unknown",
        "price": (player.get("now_cost") or 0) / 10,
        "status": AVAILABILITY_STATUSES.get(player.get("status")) or "Unknown",
        "chance_of_playing_next_round": player.get("chance_of_playing_next_round"),
    }


def prepare_captaincy_data(player: dict, match_data: dict) -> dict:
    pass


"""
match_data: dict  
position: str  
availability_status: str  
chance_of_playing_next_round: int
"""
