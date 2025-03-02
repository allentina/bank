"""
Тесты для utils.py
"""

import os
from pathlib import Path

from src.utils import read_transactions_from_json


def test_read_transactions_not_found(tmp_path: Path) -> None:
    filepath = tmp_path / "non_existent.json"
    result = read_transactions_from_json(str(filepath))
    assert result == []


def test_read_transactions_empty(tmp_path: Path) -> None:
    filepath = tmp_path / "empty.json"
    filepath.touch()
    result = read_transactions_from_json(str(filepath))
    assert result == []


def test_read_transactions_not_list(tmp_path: Path) -> None:
    filepath = tmp_path / "not_list.json"
    filepath.write_text('{"test": 123}', encoding="utf-8")
    result = read_transactions_from_json(str(filepath))
    assert result == []


def test_read_transactions_ok(tmp_path: Path) -> None:
    filepath = tmp_path / "ok.json"
    filepath.write_text('[{"id": 1}, {"id": 2}]', encoding="utf-8")
    result = read_transactions_from_json(str(filepath))
    assert len(result) == 2
    assert result[0]["id"] == 1
