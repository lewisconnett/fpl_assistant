from data.data_preparer import prepare_player_profile


def test_prepare_player_profile():
    expected_profile = {
        "name": "Cole Palmer",
        "position": "MID",
        "team": "Chelsea",
        "price": 10.8,
        "status": "Available",
        "chance_of_playing_next_round": 100,
    }

    player_payload = {
        "id": 558,
        "first_name": "Cole",
        "second_name": "Palmer",
        "web_name": "Palmer",
        "team": 6,
        "element_type": 3,
        "status": "a",  
        "chance_of_playing_next_round": 100,
        "chance_of_playing_this_round": 100,
        "news": "",
        "news_added": None,
        "now_cost": 108,
    }

    team_payload = {"id": 6, "name": "Chelsea", "short_name": "CHE", "code": 11}

    result = prepare_player_profile(player_payload, team_payload)
    
    assert result == expected_profile
