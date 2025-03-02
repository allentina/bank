"""
Тесты для external_api.py
"""

import pytest
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub


@pytest.fixture
def mock_api_key(monkeypatch):
    monkeypatch.setenv("EXCHANGE_RATES_API_KEY", "test_api_key")


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_ok(mock_get, mock_api_key):
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    # Подделываем ответ API
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "rates": {
            "RUB": 75.0
        }
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    rub_value = convert_to_rub(transaction)
    assert rub_value == 7500.0

    mock_get.assert_called_once()
    _, kwargs = mock_get.call_args
    assert kwargs["params"]["base"] == "USD"
    assert kwargs["params"]["symbols"] == "RUB"


@patch("src.external_api.requests.get")
def test_convert_to_rub_no_api_key(mock_get, monkeypatch):
    monkeypatch.delenv("EXCHANGE_RATES_API_KEY", raising=False)
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError):
        convert_to_rub(transaction)


def test_convert_to_rub_already_rub(mock_api_key):
    transaction = {
        "operationAmount": {
            "amount": "200",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 200.0
