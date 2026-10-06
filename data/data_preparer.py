from config import AVAILABILITY_STATUSES, POSITIONS


def prepare_player_profile(player: dict, team: dict) -> dict:

    chance_of_playing = player.get("chance_of_playing_next_round")

    return {
        "name": f'{player.get("first_name")} {player.get("second_name")}',
        "position": POSITIONS.get(player.get("element_type")),
        "team": team.get("name"),
        "price": player.get("now_cost") / 10,
        "status": AVAILABILITY_STATUSES.get(player.get("status")),
        "chance_of_playing_next_round": (
            chance_of_playing if chance_of_playing is not None else 100
        ),
    }


def prepare_captaincy_data(player: dict, match_data: dict) -> dict:
    pass


"""
match_data: dict  
position: str  
availability_status: str  
chance_of_playing_next_round: int
"""
