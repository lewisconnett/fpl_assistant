from core.player_search import find_player_by_name
from core.player_search import get_captain_data
from data.data_preparer import prepare_player_profile
from data.FPLDataService import FPLDataService
from ui.player_search_ui import show_player
import logging
import pyinputplus as pyip


def run_player_search(fpl_data: FPLDataService):
    """Main entry point for player search"""
    logging.info("Running player search feature")
    while True:
        player_name = pyip.inputStr("Enter player name: ").lower()

        result = search_player(player_name, fpl_data)
        print(result)

        # packaged_player = prepare_player_profile(result["data"]["player"], result)

        # show_player(packaged_player)

        continue_choice = pyip.inputYesNo(
            "Would you like to lookup another player? [Y/N]: "
        )
        if continue_choice == "no":
            logging.info(
                "Player search feature has closed. Redirecting user back to main menu"
            )
            break


def search_player(player_name: str, fpl_data: FPLDataService) -> dict:
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