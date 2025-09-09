# Автотесты для Lesson 10

Проект содержит автотесты для калькулятора и интернет-магазина с использованием Page Object Pattern и Allure отчетности.


## Установка и запуск

```bash
# Установка зависимостей
pip install -r requirements.txt

# Установка Allure
pip install allure-pytest

# Запуск всех тестов с формированием отчета
pytest --alluredir=allure-results

# Просмотр отчета
allure serve allure-results

# Запуск тестов для калькулятора
pytest tests/test_calculator.py --alluredir=allure-results

# Запуск тестов для магазина
pytest tests/test_store.py --alluredir=allure-results

# Запуск с повторением упавших тестов
pytest --reruns 2 --alluredir=allure-results

# Генерация статического отчета
allure generate allure-results -o allure-report --clean

# Открытие статического отчета (открыть файл в браузере)
allure-report/index.html