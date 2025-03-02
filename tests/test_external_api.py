import pytest
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub
from typing import Any

@pytest.fixture
def mock_api_key(monkeypatch: Any) -> None:
    monkeypatch.setenv("EXCHANGE_RATES_API_KEY", "test_api_key")


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_ok(mock_get: MagicMock, mock_api_key: None) -> None:
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    mock_response = MagicMock()
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    rub_value = convert_to_rub(transaction)
    assert rub_value == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_no_api_key(mock_get: MagicMock, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXCHANGE_RATES_API_KEY", raising=False)
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError):
        convert_to_rub(transaction)


def test_convert_to_rub_already_rub(mock_api_key: None) -> None:
    transaction = {
        "operationAmount": {
            "amount": "200",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_to_rub(transaction)
    assert result == 200.0
