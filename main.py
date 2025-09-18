import sys
from ui.menus import display_main_menu
from ui.input_helpers import get_user_choice
from data.loader import initialise_app
from core.app import handle_exit
from features.player_search import player_search

players_data = None
teams = None

def main_loop():
    global players_data, teams
    
    while True:
        try:
            display_main_menu()
            user_choice = get_user_choice()
            
            match user_choice:
                case '1':
                    player_search(players_data, teams)
                case '2':
                    # Compare two players
                    pass
                case '3':
                    # Best captain choice for upcoming GW, based on users team
                    pass
                case '4':
                    initialise_app()
                case '5':
                    handle_exit()
                
        except KeyboardInterrupt:
            print('\n\n👋 Goodbye!')
            sys.exit(0)
        except Exception as e:
            print(f'\n An unexpected error occured: {e}')
    
def main():
    global players_data, teams
    print("Welcome to FPL Assistant!")
    
    players_data, teams = initialise_app()
    if not players_data:
        print('Failed to start application. Please check your internet connection and try again!')
        sys.exit(1)
        
    main_loop()

if __name__ ==  '__main__':
    main()