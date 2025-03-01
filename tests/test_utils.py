import pytest
import os
from src.utils import read_transactions_from_json


def test_read_transactions_not_found(tmp_path):
    # Файл не существует
    filepath = str(tmp_path / "non_existing.json")
    result = read_transactions_from_json(filepath)
    assert result == []


def test_read_transactions_empty(tmp_path):
    # Создадим пустой файл
    filepath = tmp_path / "empty.json"
    filepath.touch()  # создает пустой файл
    result = read_transactions_from_json(str(filepath))
    assert result == []


def test_read_transactions_not_list(tmp_path):
    # JSON, но не список
    filepath = tmp_path / "not_list.json"
    filepath.write_text('{"key": "value"}', encoding='utf-8')
    result = read_transactions_from_json(str(filepath))
    assert result == []


def test_read_transactions_ok(tmp_path):
    # Корректный список
    filepath = tmp_path / "ok.json"
    data_str = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'

    filepath.write_text(data_str, encoding='utf-8')
    result = read_transactions_from_json(str(filepath))
    assert len(result) == 2
    assert result[0]["id"] == 1
