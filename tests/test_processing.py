import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    result = filter_by_state(data)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_sort_by_date() -> None:
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    sorted_data = sort_by_date(data, reverse=False)
    # 2018 -> 2019
    assert [item["id"] for item in sorted_data] == [2, 1]
