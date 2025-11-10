import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import square

class TestSquare(unittest.TestCase):
    
    def test_area_positive_side(self):
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(1), 1)
    
    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)
    
    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-5)
    
    def test_perimeter_positive_side(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(1), 4)
    
    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)
    
    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-3)

if __name__ == '__main__':
    unittest.main()
