import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import triangle

class TestTriangle(unittest.TestCase):
    
    def test_area_positive_values(self):
        self.assertEqual(triangle.area(6, 4), 12.0)
        self.assertEqual(triangle.area(3, 5), 7.5)
    
    def test_area_zero_values(self):
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(5, 0), 0)
    
    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            triangle.area(-6, 4)
    
    def test_perimeter_positive_sides(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(triangle.perimeter(0, 4, 5), 9)
        self.assertEqual(triangle.perimeter(3, 0, 5), 8)

if __name__ == '__main__':
    unittest.main()
