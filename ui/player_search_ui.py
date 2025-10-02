def show_player(player: dict): 
    print("\n" + "="*50)
    print(f"Player: {player['first_name']} {player['second_name']}")
    print(f"Team: {player['team']}")
    print(f"Position: {player['position']}")
    print(f"Status: {player['status']}")
    print(f"Chance of Playing Next Round: {player['chance_of_playing_next_round']}%")
    
    if player['captain_data']:
        print("\nCaptaincy Assessment:")
        print(f"Score: {player['captain_data']['score']:.2f}")
        print(f"Rating: {player['captain_data']['rating']}")
        print(f"Triple Captain Recommendation: {player['captain_data']['triple_recommendation']}")
        if 'reason' in player['captain_data']:
            print(f"Reason: {player['captain_data']['reason']}")
    
    print("="*50 + "\n")    