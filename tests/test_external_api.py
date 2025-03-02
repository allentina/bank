"""
Тесты для external_api.py
"""

import pytest
from unittest.mock import patch, MagicMock
from typing import Any

from src.external_api import convert_to_rub


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
