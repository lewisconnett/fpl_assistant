
def show_player(player: dict):

    data = player

    print("\n" + "=" * 50)
    print(f"Player: {data['first_name']} {data['second_name']}")
    print(f"Team: {data['team']}")
    print(f"Position: {data['position']}")
    print(f"Status: {data['status']}")
    print(f"Chance of Playing Next Round: {data['chance_of_playing_next_round']}%")
    print("=" * 50 + "\n")
