from data.fpl_api import (
    validate_fpl_data,
    validate_team_info,
    validate_match_info,
    validate_squad_picks,
)
import pytest


def test_validate_fpl_data_raises_if_not_dict():
    with pytest.raises(ValueError):
        validate_fpl_data(["not", "a", "dict"])


def test_validate_fpl_data_raises_if_response_body_is_empty():
    with pytest.raises(ValueError):
        validate_fpl_data({})


def test_validate_team_info_raises_if_not_dictionary():
    with pytest.raises(ValueError):
        validate_team_info(["not", "a", "dictionary"])


def test_validate_team_info_raises_if_response_body_is_empty():
    with pytest.raises(ValueError):
        validate_team_info({})


def test_validate_match_data_raises_if_not_dict():
    with pytest.raises(ValueError):
        validate_match_info(["not", "a", "dict"])


def test_validate_match_data_raises_if_repsonse_body_is_empty():
    with pytest.raises(ValueError):
        validate_match_info({})


def test_validate_squad_data_raises_if_not_dict():
    with pytest.raises(ValueError):
        validate_squad_picks(["not", "a", "dict"])


def test_validate_squad_data_if_response_body_is_empty():
    with pytest.raises(ValueError):
        validate_squad_picks({})
