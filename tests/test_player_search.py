from features.player_search import search_player
from data.global_data import FPLData

import pytest


def test_if_no_player_found_raise_value_error():
    raw_data = {
        "elements": [
            {"id": 1, "first_name": "Cole", "second_name": "Palmer"},
            {"id": 2, "first_name": "Bakayo", "second_name": "Saka"},
        ]
    }

    fpl_data = FPLData(raw_data)

    with pytest.raises(ValueError):
        search_player("haaland", fpl_data)
