"""
Реализует чтение финансовых операций из CSV и XLSX-файлов.
"""

from typing import List, Dict, Any

import pandas as pd


def read_transactions_from_csv(filepath: str) -> List[Dict[str, Any]]:
    """
    Считывает CSV-файл d список словарей.
    """
    df = pd.read_csv(filepath, encoding="utf-8")
    return df.to_dict(orient="records")


def read_transactions_from_excel(filepath: str) -> List[Dict[str, Any]]:
    """
    Считывает Excel (XLSX) d список словарей
    """
    df = pd.read_excel(filepath, engine="openpyxl")  # для .xlsx
    return df.to_dict(orient="records")
