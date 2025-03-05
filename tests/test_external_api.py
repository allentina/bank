"""
Тесты для external_api.py
"""

import pytest
from typing import Any, Dict
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub


@pytest.fixture
def mock_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("EXCHANGE_RATES_API_KEY", "fake_key")


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_ok(mock_get: MagicMock, mock_api_key: None) -> None:
    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = mock_response

    rub_value = convert_to_rub(transaction)
    assert rub_value == 7500.0


def test_convert_to_rub_missing_data() -> None:
    # Нет amount/currency => 0.0
    assert convert_to_rub({}) == 0.0


def test_convert_to_rub_rub() -> None:
    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "500",
            "currency": {"code": "RUB"}
        }
    }
    assert convert_to_rub(transaction) == 500.0


def test_convert_to_rub_no_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXCHANGE_RATES_API_KEY", raising=False)
    transaction = {
        "operationAmount": {
            "amount": "200",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError, match="API key for exchange rates not found."):
        convert_to_rub(transaction)


@patch("src.external_api.requests.get")
def test_convert_to_rub_raise_for_status(mock_get: MagicMock, mock_api_key: None) -> None:
    transaction = {
        "operationAmount": {
            "amount": "300",
            "currency": {"code": "USD"}
        }
    }
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("404 Not Found")
    mock_get.return_value = mock_response

    with pytest.raises(Exception, match="404 Not Found"):
        convert_to_rub(transaction)
