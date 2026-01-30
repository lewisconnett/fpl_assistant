def show_player(player: dict):
    if not player.get('success'):
        print(player.get('message'))
        return
    
    data = player.get('data')
    
    print("\n" + "="*50)
    print(f"Player: {data['first_name']} {data['second_name']}")
    print(f"Team: {data['team']}")
    print(f"Position: {data['position']}")
    print(f"Status: {data['status']}")
    print(f"Chance of Playing Next Round: {data['chance_of_playing_next_round']}%")
    
    if data['captain_data']:
        print("\nCaptaincy Assessment:")
        print(f"Score: {data['captain_data']['score']:.2f}")
        print(f"Rating: {data['captain_data']['rating']}")
        print(f"Triple Captain Recommendation: {data['captain_data']['triple_recommendation']}")
        if 'reason' in data['captain_data']:
            print(f"Reason: {data['captain_data']['reason']}")
    
    print("="*50 + "\n")    