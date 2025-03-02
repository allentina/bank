
import json
from pathlib import Path
from src.utils import read_transactions_from_json
from typing import Any


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
    transactions = [{"id": 1}, {"id": 2}]
    filepath.write_text(json.dumps(transactions), encoding="utf-8")
    result = read_transactions_from_json(str(filepath))
    assert isinstance(result, list)
    assert len(result) == 2
