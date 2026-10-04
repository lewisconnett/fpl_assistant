from core.player_search import find_player_by_name
from config import POSITIONS, AVAILABILITY_STATUSES
from core.player_search import get_captain_data
from data.global_data import FPLData
from ui.player_search_ui import show_player
import logging
import pyinputplus as pyip


def run_player_search(fpl_data: FPLData):
    """Main entry point for player search"""
    logging.info("Running player search feature")
    while True:
        player_name = pyip.inputStr("Enter player name: ").lower()

        result = search_player(player_name, fpl_data)

        packaged_player = build_player_profile(result["data"])

        show_player(packaged_player)

        continue_choice = pyip.inputYesNo(
            "Would you like to lookup another player? [Y/N]: "
        )
        if continue_choice == "no":
            logging.info(
                "Player search feature has closed. Redirecting user back to main menu"
            )
            break


def search_player(player_name: str, fpl_data: FPLData) -> dict:
    """Get player"""

    try:
        player = find_player_by_name(player_name, fpl_data)
    except ValueError as e:
        return {"success": False, "message": str(e), "data": None}

    team = fpl_data.get_team_by_id(player["team"])

    return {
        "success": True,
        "message": f"Player found for {player['web_name']}",
        "data": {"player": player, "team": team},
    }


def add_captain_data(player):
    # TODO: need to get captain data and then package player profile, write tests for this feature
    pass


def build_player_profile(data: dict) -> dict:
    player = data["player"]
    team = data["team"]

    player_id = player.get("id")
    logging.info("Packaging data for player ID: %s", player_id)

    chance_of_playing = player.get("chance_of_playing_next_round")

    profile = {
        "first_name": player.get("first_name"),
        "second_name": player.get("second_name"),
        "position": POSITIONS.get(player.get("element_type")),
        "team": team.get("name"),
        "status": AVAILABILITY_STATUSES.get(player.get("status")),
        "chance_of_playing_next_round": (
            chance_of_playing if chance_of_playing is not None else 100
        ),
    }

    logging.info("Successfully created player profile for player ID: %s", player_id)

    return profile
