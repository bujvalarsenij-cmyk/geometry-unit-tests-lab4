# Geometry Library - Лабораторная работа №4

Библиотека для вычисления площадей и периметров геометрических фигур с комплектом unit-тестов.

## 📁 Структура проекта

- `src/` - исходный код библиотеки
- `tests/` - unit-тесты
- `docs/` - документация

## 🛠 Установка и запуск

### Запуск тестов
```bash
# Все тесты
py tests/run_all_tests.py

# Отдельные тесты
py -m unittest tests.test_circle -v
py -m unittest tests.test_rectangle -v
py -m unittest tests.test_square -v
py -m unittest tests.test_triangle -v

# Через discover
py -m unittest discover tests/ -v
