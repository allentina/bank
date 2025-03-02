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

## Модуль decorators

Реализован декоратор `log`, который автоматически логирует результат вызова функции (успешно / с ошибкой).

### Использование

```python
from src.decorators import log

@log()  # вывод логов в консоль
def add(a, b):
    return a + b

@log(filename="mylog.txt")  # вывод логов в файл
def sub(a, b):
    return a - b

## Функционал

1. **Чтение JSON-файла** (`src/utils.py`):
   - Функция `read_transactions_from_json(filepath: str) -> List[Dict]]` 
   - Возвращает список транзакций (списков словарей) или `[]`, если файл пустой/битый/не найден.

2. **Конвертация валют** (`src/external_api.py`):
   - Функция `convert_to_rub(transaction: dict) -> float`
   - Если `transaction["operationAmount"]["currency"]["code"] == "RUB"`, возвращает `amount` как есть.
   - Если `USD`/`EUR`, запрашивает курс у API (Exchangerates Data API) и умножает сумму на курс рубля.
   - Токен для API берется из переменной окружения `EXCHANGE_RATES_API_KEY`.

## Окружение

- В корне репозитория лежит `.env.example` (шаблон).
- Добавьте свой ключ API в `.env` (не пушьте в GitHub!).

## Тесты

- **test_utils.py** — тесты для функции чтения JSON.
- **test_external_api.py** — тесты для конвертации валют (mock/patch, фикстура env).
- Запуск:
  ```bash
  pytest
  coverage run -m pytest
  coverage report
  coverage html
