import unittest
import sys
import os

# Получаем абсолютный путь к корню проекта
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

try:
    from src import circle
    print("OK: Импорт circle успешен")
except ImportError as e:
    print(f"ERROR: Ошибка импорта circle: {e}")
    # Альтернативный способ импорта
    sys.path.insert(0, os.path.join(parent_dir, 'src'))
    import circle

class TestCircle(unittest.TestCase):
    
    def test_area_positive_radius(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483, places=5)
        self.assertAlmostEqual(circle.area(1), 3.141592653589793, places=5)
    
    def test_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
    
    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-5)
    
    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793, places=5)
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586, places=5)
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)

if __name__ == '__main__':
    unittest.main()
