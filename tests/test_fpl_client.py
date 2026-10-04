import pytest
from data.FPLClient import FPLClient
from unittest.mock import Mock
from config import ELEMENT_SUMMARY, ENTRY_INFO, SQUAD_PICKS


def test_validate_data():
    client = FPLClient()
    payload = {"elements": []}

    result = client._validate_data(payload)

    assert result == payload


def test_validate_data_is_not_dict():
    client = FPLClient()
    mock_payload = []

    with pytest.raises(ValueError):
        client._validate_data(mock_payload)


def test_fetch_element_summary():
    client = FPLClient()
    payload = {"history": [], "fixtures": []}

    fake_response = Mock()
    fake_response.json.return_value = payload
    client.session.get = Mock(return_value=fake_response)

    result = client.fetch_element_summary(player_id=42)

    expected_url = ELEMENT_SUMMARY.format(player_id=42)
    assert result == payload

    client.session.get.assert_called_once_with(expected_url)
    fake_response.raise_for_status.assert_called_once()


def test_fetch_manager_info():
    client = FPLClient()
    payload = {"id": 12, "name": "chelsea daggers"}

    fake_response = Mock()
    fake_response.json.return_value = payload
    client.session.get = Mock(return_value=fake_response)

    result = client.fetch_manager_info(entry_id=6749321)

    expected_url = ENTRY_INFO.format(entry_id=6749321)
    assert result == payload

    client.session.get.assert_called_once_with(expected_url)
    fake_response.raise_for_status.assert_called_once()


def test_fetch_squad_picks():
    client = FPLClient()
    payload = {"picks": [{"element": 351}, {"element": 342}]}

    fake_response = Mock()
    fake_response.json.return_value = payload
    client.session.get = Mock(return_value=fake_response)

    result = client.fetch_squad_picks(entry_id=6749321,gw=3)

    expected_url = SQUAD_PICKS.format(entry_id=6749321,gw=3)
    assert result == payload
    
    client.session.get.assert_called_once_with(expected_url)
    fake_response.raise_for_status.assert_called_once()
