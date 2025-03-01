# Bank Masking Project

## Описание проекта
Данный проект предназначен для демонстрации простого виджета банковских операций.  
Включает функции маскировки карт/счетов, фильтрации по статусу транзакции и сортировки по дате.

## Структура репозитория
- **src/masks.py** — функции для маскировки карт и счетов.
- **src/widget.py** — функции `mask_account_card` и `get_date`.
- **src/processing.py** — функции `filter_by_state` и `sort_by_date`.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/<username>/bank-masking-project.git
   
## Модуль generators

В модуле `generators.py` находятся функции, позволяющие обрабатывать большие объёмы данных транзакций с помощью генераторов:

1. **filter_by_currency(transactions, currency_code)**  
   - Принимает список транзакций и код валюты, возвращает итератор (генератор), 
     выдающий только те транзакции, у которых `currency['code']` совпадает с `currency_code`.
   ```python
   from src.generators import filter_by_currency

   transactions = [...]  # список словарей
   usd_transactions = filter_by_currency(transactions, "USD")
   for t in usd_transactions:
       print(t)  # выведутся только USD-транзакции
