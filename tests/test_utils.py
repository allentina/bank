"""
Тесты для utils.py
"""

import json
from pathlib import Path
from src.utils import read_transactions_from_json


def test_read_transactions_not_found(tmp_path: Path) -> None:
    filepath = tmp_path / "no_file.json"
    assert read_transactions_from_json(str(filepath)) == []


def test_read_transactions_empty(tmp_path: Path) -> None:
    filepath = tmp_path / "empty.json"
    filepath.touch()
    assert read_transactions_from_json(str(filepath)) == []


def test_read_transactions_not_list(tmp_path: Path) -> None:
    filepath = tmp_path / "not_list.json"
    filepath.write_text('{"test": 123}', encoding="utf-8")
    assert read_transactions_from_json(str(filepath)) == []


def test_read_transactions_ok(tmp_path: Path) -> None:
    filepath = tmp_path / "ok.json"
    data = [{"id": 1}, {"id": 2}]
    filepath.write_text(json.dumps(data), encoding="utf-8")
    assert read_transactions_from_json(str(filepath)) == data


def test_read_transactions_bad_json(tmp_path: Path) -> None:
    filepath = tmp_path / "bad.json"
    filepath.write_text('{"id": ', encoding="utf-8")  # сломан JSON
    assert read_transactions_from_json(str(filepath)) == []
