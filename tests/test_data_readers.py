"""
Тесты для новых функций чтения CSV/XLSX.
Используем Mock и patch, чтобы не читать файлы реально.
"""

import pytest
from typing import List, Dict, Any
from unittest.mock import patch, MagicMock
from src.data_readers import read_transactions_from_csv, read_transactions_from_excel


@pytest.mark.parametrize("fake_data", [
    [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}],
    [],
])
@patch("src.data_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv: MagicMock, fake_data: List[Dict[str, Any]]) -> None:
    """
    Тест функции read_transactions_from_csv:
    - mock-им pd.read_csv
    - проверяем, что результат совпадает с fake_data
    """
    df_mock = MagicMock()
    df_mock.to_dict.return_value = fake_data
    mock_read_csv.return_value = df_mock

    result = read_transactions_from_csv("dummy.csv")
    assert result == fake_data


@pytest.mark.parametrize("fake_data", [
    [{"id": 10, "description": "Payment"}, {"id": 20, "description": "Refund"}],
    [],
])
@patch("src.data_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel: MagicMock, fake_data: List[Dict[str, Any]]) -> None:
    """
    Тест функции read_transactions_from_excel:
    - mock-им pd.read_excel
    - проверяем, что результат совпадает с fake_data
    """
    df_mock = MagicMock()
    df_mock.to_dict.return_value = fake_data
    mock_read_excel.return_value = df_mock

    result = read_transactions_from_excel("dummy.xlsx")
    assert result == fake_data
