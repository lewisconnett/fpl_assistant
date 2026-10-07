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

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_if_data_missing():
    expected_profile = {
        "name": "Unknown",
        "position": "Unknown",
        "team": "Unknown",
        "price": 0,
        "status": "Unknown",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "id": None,
        "first_name": None,
        "second_name": None,
        "web_name": None,
        "team": None,
        "element_type": None,
        "status": None,
        "chance_of_playing_next_round": None,
        "chance_of_playing_this_round": None,
        "news": "",
        "news_added": None,
        "now_cost": None,
    }

    team_payload = {"id": None, "name": None, "short_name": None, "code": None}

    result = prepare_player_profile(player_payload, team_payload)

    assert result == expected_profile


def test_prepare_player_profile_if_some_keys_are_missing():
    expected_profile = {
        "name": "Palmer",
        "position": "MID",
        "team": "Chelsea",
        "price": 10.8,
        "status": "Unknown",
        "chance_of_playing_next_round": 100,
    }

    player_payload = {
        "id": 558,
        "first_name": "Cole",
        "web_name": "Palmer",
        "team": 6,
        "element_type": 3,
        "chance_of_playing_next_round": 100,
        "chance_of_playing_this_round": 100,
        "news": "",
        "news_added": None,
        "now_cost": 108,
    }

    team_payload = {"id": 6, "name": "Chelsea", "short_name": "CHE", "code": 11}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_mononym_player():
    """Tests players who go by a single name (e.g., Savinho) where first/second names are blank or None."""
    expected_profile = {
        "name": "Savinho",
        "position": "MID",
        "team": "Man City",
        "price": 6.5,
        "status": "Available",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "first_name": None,
        "second_name": None,
        "web_name": "Savinho",
        "element_type": 3,
        "status": "a",
        "now_cost": 65,
    }
    team_payload = {"name": "Man City", "short_name": "MCI"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_keys_completely_absent():
    """Tests absolute minimum payloads where required keys are completely missing from the dictionaries."""
    expected_profile = {
        "name": "Unknown",
        "position": "Unknown",
        "team": "Unknown",
        "price": 0,
        "status": "Unknown",
        "chance_of_playing_next_round": None,
    }

    player_payload = {}
    team_payload = {}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_unmapped_position_element_type():
    """Tests when an element_type integer is provided but doesn't exist in the POSITIONS map."""
    expected_profile = {
        "name": "Saka",
        "position": "Unknown",
        "team": "Arsenal",
        "price": 10.0,
        "status": "Unknown",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "web_name": "Saka",
        "element_type": 99,  # Unmapped position ID
        "now_cost": 100,
    }
    team_payload = {"name": "Arsenal"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_unmapped_status_code():
    """Tests when a status code is provided but doesn't exist in the AVAILABILITY_STATUSES map."""
    expected_profile = {
        "name": "Salah",
        "position": "MID",
        "team": "Liverpool",
        "price": 12.5,
        "status": "Unknown",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "web_name": "Salah",
        "element_type": 3,
        "status": "z",  # Unmapped status letter
        "now_cost": 125,
    }
    team_payload = {"name": "Liverpool"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_team_name_missing_uses_short_name():
    """Tests the team fallback chain when the full name is missing but short_name is populated."""
    expected_profile = {
        "name": "Isak",
        "position": "FWD",
        "team": "NEW",
        "price": 8.5,
        "status": "Available",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "web_name": "Isak",
        "element_type": 4,
        "status": "a",
        "now_cost": 85,
    }
    team_payload = {"name": None, "short_name": "NEW"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_chance_of_playing_is_explicitly_zero():
    """Verifies that a valid 0% chance of playing is preserved and not overwritten by a default 100% value."""
    expected_profile = {
        "name": "James",
        "position": "DEF",
        "team": "Chelsea",
        "price": 5.0,
        "status": "Injured",
        "chance_of_playing_next_round": 0,
    }

    player_payload = {
        "web_name": "James",
        "element_type": 2,
        "status": "i",
        "now_cost": 50,
        "chance_of_playing_next_round": 0,
    }
    team_payload = {"name": "Chelsea"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_player_cost_is_zero():
    """Tests edge case where price value equals zero (e.g. unpriced structural or test assets)."""
    expected_profile = {
        "name": "Trialist",
        "position": "GK",
        "team": "Spurs",
        "price": 0.0,
        "status": "Unknown",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "web_name": "Trialist",
        "element_type": 1,
        "now_cost": 0,
    }
    team_payload = {"name": "Spurs"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_empty_string_names():
    """Verifies fallback behaviour when first and second name exist as keys but are empty strings."""
    expected_profile = {
        "name": "Son",
        "position": "MID",
        "team": "Spurs",
        "price": 10.0,
        "status": "Available",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "first_name": "",
        "second_name": "",
        "web_name": "Son",
        "element_type": 3,
        "status": "a",
        "now_cost": 100,
    }
    team_payload = {"name": "Spurs"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile


def test_prepare_player_profile_numerical_strings_for_ids():
    """Verifies dictionary lookups if element_type payload data accidentally passes numeric string identifiers."""
    expected_profile = {
        "name": "Haarez",
        "position": "Unknown",
        "team": "Arsenal",
        "price": 8.0,
        "status": "Available",
        "chance_of_playing_next_round": None,
    }

    player_payload = {
        "web_name": "Haarez",
        "element_type": "3",  # String instead of int
        "status": "a",
        "now_cost": 80,
    }
    team_payload = {"name": "Arsenal"}

    assert prepare_player_profile(player_payload, team_payload) == expected_profile