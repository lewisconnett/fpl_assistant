from unittest.mock import Mock

import pytest
from core import player_search
from core.player_search import find_player_by_name


def test_find_player_by_name_returns_matching_player():
    palmer = {"first_name": "Cole", "second_name": "Palmer", "web_name": "Palmer"}

    saka = {"first_name": "Bakayo", "second_name": "Saka", "web_name": "Saka"}

    fpl_player_data = Mock()
    fpl_player_data = [palmer, saka]

    result = find_player_by_name("Cole Palmer", fpl_player_data)

    assert result == palmer


def test_find_player_by_name_raises_value_error_if_no_match_is_found():
    raw_data = {
        "elements": [
            {"id": 1, "first_name": "Cole", "second_name": "Palmer"},
            {"id": 2, "first_name": "Bakayo", "second_name": "Saka"},
        ]
    }

    fpl_player_data = Mock()
    fpl_player_data = raw_data["elements"]

    with pytest.raises(ValueError):
        find_player_by_name("haaland", fpl_player_data)


def test_find_player_by_name_raises_when_score_is_below_threshold(monkeypatch):
    players = [
        {"first_name": "Cole", "second_name": "Palmer", "web_name": "Palmer"},
        {"first_name": "Bukayo", "second_name": "Saka", "web_name": "Saka"},
    ]
    monkeypatch.setattr(player_search, "FUZZY_MATCH_MIN_SCORE", 101)

    with pytest.raises(ValueError, match="Fuzzy match score below threshold"):
        player_search.find_player_by_name("Cole Palmer", players)
