import sys

from src.my_funcs import read_transactions_from_json
from src.data_readers import read_transactions_from_csv, read_transactions_from_excel
from src.filters import search_transactions_by_description, count_operations_by_category


def main() -> None:
    print("Привет! Добро пожаловать в программу.")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. XLSX-файл")

    choice = input("Ваш выбор: ").strip()
    if choice not in ("1", "2", "3"):
        print("Некорректный выбор. Выходим.")
        sys.exit(0)

    if choice == "1":
        path = input("Путь к JSON: ").strip()
        transactions = read_transactions_from_json(path)
        print("Выбран JSON.")
    elif choice == "2":
        path = input("Путь к CSV: ").strip()
        transactions = read_transactions_from_csv(path)
        print("Выбран CSV.")
    else:
        path = input("Путь к XLSX: ").strip()
        transactions = read_transactions_from_excel(path)
        print("Выбран XLSX.")

    if not transactions:
        print("Файл пуст/невалиден. Завершение.")
        sys.exit(0)

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status_input = input("Введите статус (EXECUTED/CANCELED/PENDING): ").strip().upper()
        if status_input in valid_statuses:
            break
        print(f"Статус {status_input} недоступен.")

    transactions = [tx for tx in transactions if tx.get("state", "").upper() == status_input]
    if not transactions:
        print("Нет транзакций с таким статусом.")
        sys.exit(0)

    sort_resp = input("Отсортировать по дате? (да/нет): ").strip().lower()
    if sort_resp == "да":
        order_resp = input("по возрастанию / по убыванию?: ").strip().lower()
        reverse_flag = (order_resp == "по убыванию")
        transactions.sort(key=lambda x: x.get("date", ""), reverse=reverse_flag)

    rub_resp = input("Только рублёвые? (да/нет): ").strip().lower()
    if rub_resp == "да":
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    find_resp = input("Искать по описанию (re)? (да/нет): ").strip().lower()
    if find_resp == "да":
        search_str = input("Введите строку поиска: ").strip()
        transactions = search_transactions_by_description(transactions, search_str)

    cat_resp = input("Подсчитать категории? (да/нет): ").strip().lower()
    if cat_resp == "да":
        categories = ["Перевод", "Оплата", "Вклад"]  # пример
        cat_dict = count_operations_by_category(transactions, categories)
        print("Счётчик категорий:", cat_dict)

    print("Итоговый список:")
    if not transactions:
        print("Ничего не найдено.")
        sys.exit(0)

    print(f"Всего {len(transactions)} транзакций:")
    for tx in transactions:
        date_str = tx.get("date", "")
        desc = tx.get("description", "")
        print(f"{date_str} {desc}")
        if "from" in tx:
            print(f"{tx['from']} -> {tx.get('to','')}")
        amount = tx.get("operationAmount", {}).get("amount", "")
        curr = tx.get("operationAmount", {}).get("currency", {}).get("code", "")
        print(f"Сумма: {amount} {curr}")
    print("Конец программы.")
