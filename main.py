import sys
import pyinputplus as pyip
from data.global_data import FPLData
from ui.menus import display_main_menu
from data.loader import initialise_app
from core.app import handle_exit
from features.player_search import run_player_search
from features.squad_captain_optimiser import run_captaincy_optimiser
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture everything
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="fpl_tool.log",
)


def main_loop(fpl_data: FPLData):
    while True:
        try:
            display_main_menu()
            user_choice = pyip.inputMenu(
                [
                    "🔍 Player Lookup",
                    "⚖️  Compare Players",
                    "👑 Squad Captain Optimiser",
                    "🔄 Refresh Data",
                    "❌ Exit",
                ],
                numbered=True,
            )

            match user_choice:
                case "🔍 Player Lookup":
                    run_player_search(fpl_data)
                case "⚖️  Compare Players":
                    pass  # compare players
                case "👑 Squad Captain Optimiser":
                    run_captaincy_optimiser()
                case "🔄 Refresh Data":
                    initialise_app()
                case "❌ Exit":
                    handle_exit()

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n An unexpected error occured: {e}")


def main():
    print("Welcome to FPL Assistant!")
    logging.info("Starting FPL Assitant")
    fpl_data = initialise_app()

    if fpl_data is not None:
        print("Data loaded successfully")
        logging.info("Successuflly loaded FPL app state")
        main_loop(fpl_data)
    else:
        print(
            "Failed to start application. Please check your internet connection and try again later!"
        )
        logging.warning("Could not start application")
        sys.exit(1)


if __name__ == "__main__":
    main()
