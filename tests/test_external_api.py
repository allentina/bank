import pytest
import requests
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
    # 100 USD -> 75.0 rate -> 7500
    assert rub_value == 7500.0

    # Проверим, что get был вызван с правильными параметрами
    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args

    # Теперь правильно проверяем словарь params:
    assert kwargs["params"]["base"] == "USD"
    assert kwargs["params"]["symbols"] == "RUB"
