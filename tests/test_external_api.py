"""
Тесты для external_api.py
"""

import pytest
from typing import Any, Dict
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub


@pytest.fixture
def mock_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Устанавливает тестовый ключ EXCHANGE_RATES_API_KEY.
    """
    monkeypatch.setenv("EXCHANGE_RATES_API_KEY", "test_key")


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_ok(mock_get: MagicMock, mock_api_key: None) -> None:
    """
    Проверяем, что при валюте USD и существующем ключе API функция корректно конвертирует.
    """
    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    # Поддельный ответ API
    response_mock = MagicMock()
    response_mock.status_code = 200
    response_mock.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = response_mock

    rub_value = convert_to_rub(transaction)
    assert rub_value == 7500.0  # 100 * 75


def test_convert_to_rub_no_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Проверяем, что при отсутствии EXCHANGE_RATES_API_KEY выбрасывается ValueError.
    """
    monkeypatch.delenv("EXCHANGE_RATES_API_KEY", raising=False)
    transaction: Dict[str, Any] = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    with pytest.raises(ValueError, match="API key for exchange rates not found."):
        convert_to_rub(transaction)
        