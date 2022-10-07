## Description

Тесты для функции, которая, используя API-worldclock, возвращает текущий год. Отчет о покрытии кода лежит в директории htmlcov.

## Requirements

Для запуска необходимо установить пакеты:

* pytest
* pytest-cov

## Run

Для запуска тестов в терминале из директории issue05 использовать команду:

```bash
pytest -v test_what_is_year_now.py   
```

Для формирования html-отчета покрытия кода в терминале из директории issue05 использовать команду:

```bash
 pytest --cov=what_is_year_now --cov-report html
```
