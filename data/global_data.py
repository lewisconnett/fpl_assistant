player_data = None
team_data = None

def init_data(players, teams):
    global player_data, team_data
    player_data = players
    team_data = teams
    
def get_player_data():
    if player_data is None:
        raise ValueError('Player data has not been initialised')
    else:
        return player_data

def get_team_data():
    if team_data is None:
        raise ValueError('Team data has not been initialised')
    else:
        return team_data

def update_player_data(new_player_data=None, new_team_data=None):
    global player_data, team_data
    
    if not new_player_data:
        player_data = new_player_data
    
    if not new_team_data:
        team_data = new_team_data