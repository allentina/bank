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