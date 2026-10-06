import pytest

from data.FPLDataService import FPLDataService


def test_players_raise_if_elements_not_in_raw_data():
    raw_data = {"chips": [], "teams": []}

    fpl_data = FPLDataService(raw_data)

    with pytest.raises(ValueError):
        _ = fpl_data.players


def test_players_returns_players_list_when_valid():
    raw_data = {
        "elements": [
            {"id": 1, "web_name": "Palmer"},
            {"id": 2, "web_name": "Saka"},
        ]
    }

    fpl_data = FPLDataService(raw_data)

    assert fpl_data.players == raw_data["elements"]
    assert isinstance(fpl_data.players, list)


def test_players_raises_if_elements_empty_in_raw_data():
    raw_data = {"chips": [], "teams": [], "elements": []}

    fpl_data = FPLDataService(raw_data)

    with pytest.raises(ValueError):
        _ = fpl_data.players


def test_players_is_cached_after_first_access():
    raw_data = {
        "elements": [
            {"id": 1, "web_name": "Palmer"},
            {"id": 2, "web_name": "Saka"},
        ]
    }

    fpl_data = FPLDataService(raw_data)

    first = fpl_data.players
    second = fpl_data.players

    assert first is second


def test_teams_returns_teams_list_when_valid():
    raw_data = {
        "teams": [
            {"code": 1, "name": "Chelsea"},
            {"code": 2, "name": "Manchester City"},
        ]
    }

    fpl_data = FPLDataService(raw_data)

    assert fpl_data.teams == raw_data["teams"]
    assert isinstance(fpl_data.teams, list)


def test_teams_raise_if_teams_not_in_raw_data():
    raw_data = {"chips": [], "elements": []}

    fpl_data = FPLDataService(raw_data)

    with pytest.raises(ValueError):
        _ = fpl_data.teams


def test_teams_raise_if_teams_empty_in_raw_data():
    raw_data = {"chips": [], "teams": [], "elements": []}

    fpl_data = FPLDataService(raw_data)

    with pytest.raises(ValueError):
        _ = fpl_data.teams


def test_teams_is_cached_after_first_access():
    raw_data = {
        "teams": [
            {"code": 1, "name": "Chelsea"},
            {"code": 2, "name": "Manchester City"},
        ]
    }

    fpl_data = FPLDataService(raw_data)

    first = fpl_data.teams
    second = fpl_data.teams

    assert first is second
