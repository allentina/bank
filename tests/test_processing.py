import pytest
from src.processing import sort_by_date

def test_sort_by_date_incorrect():
    bad_data = [{'id': 999, 'state': 'EXECUTED', 'date': 'НекорректнаяДата'}]
    with pytest.raises(ValueError):
        sort_by_date(bad_data)