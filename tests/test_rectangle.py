import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import rectangle

class TestRectangle(unittest.TestCase):
    
    def test_area_positive_sides(self):
        self.assertEqual(rectangle.area(4, 6), 24)
        self.assertEqual(rectangle.area(3, 7), 21)
    
    def test_area_zero_sides(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(5, 0), 0)
    
    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4, 6)
    
    def test_perimeter_positive_sides(self):
        self.assertEqual(rectangle.perimeter(4, 6), 20)
        self.assertEqual(rectangle.perimeter(3, 7), 20)
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(5, 0), 10)

if __name__ == '__main__':
    unittest.main()
