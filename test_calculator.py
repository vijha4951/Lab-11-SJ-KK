# https://github.com/vijha4951/Lab-11-SJ-KK
# Partner 1: Sannvi Jha
# Partner 2: Kaushik

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    #addition unit tests
    def test_add(self):
        self.assertEqual(add(3, 3), 6)
        self.assertEqual(add(-5, 6), 1)
        self.assertEqual(add(0, 0), 0)
    #subtraction unit tests 
    def test_subtract(self):
        self.assertEqual(subtract(11, 5), 6)
        self.assertEqual(subtract(4, 9), -5)
        self.assertEqual(subtract(0, 0), 0)

    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 8), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, 20), 5)
        self.assertEqual(divide(-2, 10), -5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
    #logrithmic unit test 
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 81), 4)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(16), 4)

    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
