# Geometry Library - Лабораторная работа №4

Библиотека для вычисления площадей и периметров геометрических фигур с комплектом unit-тестов.

## 📁 Структура проекта
- `src/` - исходный код библиотеки
- `tests/` - unit-тесты  
- `docs/` - документация и отчёты

## 🧪 Результаты тестирования
Все 24 теста успешно пройдены:
- ✅ circle: 6 тестов
- ✅ rectangle: 6 тестов
- ✅ square: 6 тестов  
- ✅ triangle: 6 тестов

## 🛠 Запуск тестов
```bash
# Все тесты
py tests/run_all_tests.py

# Через unittest discover
py -m unittest discover tests/ -v

# Отдельные тесты
py -m unittest tests.test_circle -v
py -m unittest tests.test_rectangle -v
py -m unittest tests.test_square -v
py -m unittest tests.test_triangle -v

📊 Функциональность
circle: площадь и длина окружности

rectangle: площадь и периметр прямоугольника

square: площадь и периметр квадрата

triangle: площадь треугольника и периметр

👨‍💻 Автор
Буйвал Арсений
M3121
