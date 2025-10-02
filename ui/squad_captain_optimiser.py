import pyinputplus as pyip

def show_menu():
    print('Squad Captain Optimiser: ')
    
def check_users_team(team_info):
    print(f'Team Name: {team_info['name']}, {team_info['player_region_iso_code_long']}')

def handle_wrong_team():
    print('Thanks for letting us know. Please double-check your team ID and try again.')
    
    need_help = pyip.inputYesNo('Need help on how to find your team ID [Y/N]: ')
    
    if need_help == 'yes':
         # Instructions to help users get their team ID
        print('''
              🔎 How to Find Your Correct FPL Team ID
              
              1. Visit the official Fantasy Premier League website and log in to your account.
              2. Go to the “Pick Team” tab in the top menu.
              3. Scroll down and click on “Transfer History” or “Gameweek History” on the left-hand side.
              4. Look at your browser’s URL bar at the top of the screen.
              5. Find the number that appears after /entry/ and before /transfers/ in the URL.
              💡 This number is your unique FPL Team ID.
              6. Copy that number and enter it here ✅.
              
              Example:
              If your URL looks like:
              "https://fantasy.premierleague.com/entry/21918/transfers"
              then your Team ID is 21918.
              
              ''')
        
def display_best_captain_pick(result):
    '''Display captain recommendation with formatting'''
    print('\n' + '='*50)
    
    if not result['success']:
        print(f'❌ {result['message']}')
        print('='*50)
        return
    
    data = result['data']
    
    print(f'🎯 CAPTAIN RECOMMENDATION FOR GAMEWEEK')
    print('='*50)
    print(f'\n✨ BEST CHOICE: {data['player_name']}')
    print(f'   Our Captain Score: {data['score']:.1f}\n')
    
    if len(data['alternatives']) > 1:
        print('📊 ALTERNATIVE OPTIONS:')
        for i, (name, score_data) in enumerate(data['alternatives'][1:4], 2):
            print(f'   {i}. {name}: {score_data['score']:.1f}')
    
    print('\n' + '='*60)