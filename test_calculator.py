import unittest
from Calculator import add, subtract, multiply, divide, square_root, power, sin, cos, tan, log, ln, factorial, degrees_to_radians, radians_to_degrees, permutation, combination, absolute, gcd, lcm
import math

class TestCalculatorFunctions(unittest.TestCase):

    # Test for add function
    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-3, -2), -5)

    # Test for subtract function
    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-3, -2), -1)

    # Test for multiply function
    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-3, -2), 6)

    # Test for divide function
    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(3, -3), -1)
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)

    # Test for square root function
    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-4)  # Error for negative numbers

    # Test for power function
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(10, -1), 0.1)

    # Test for sin function
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(30), 0.5, places=2)
        self.assertAlmostEqual(sin(90), 1)

    # Test for cos function
    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(60), 0.5, places=2)
        self.assertAlmostEqual(cos(90), 0)

    # Test for tan function
    def test_tan(self):
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(30), 0.577, places=3)

    # Test for log (base 10) function
    def test_log(self):
        self.assertEqual(log(10), 1)
        self.assertEqual(log(100), 2)
        with self.assertRaises(ValueError):  # Log of non-positive numbers is not defined
            log(0)
        with self.assertRaises(ValueError):
            log(-1)

    # Test for natural log (ln) function
    def test_ln(self):
        self.assertEqual(ln(math.e), 1)
        with self.assertRaises(ValueError):  # Log of non-positive numbers is not defined
            ln(0)
        with self.assertRaises(ValueError):
            ln(-1)

    # Test for factorial function
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    # Test for degrees to radians function
    def test_degrees_to_radians(self):
        self.assertEqual(degrees_to_radians(180), math.pi)
        self.assertEqual(degrees_to_radians(90), math.pi / 2)

    # Test for radians to degrees function
    def test_radians_to_degrees(self):
        self.assertEqual(radians_to_degrees(math.pi), 180)
        self.assertEqual(radians_to_degrees(math.pi / 2), 90)

    # Test for permutation function
    def test_permutation(self):
        self.assertEqual(permutation(5, 3), 60)
        self.assertEqual(permutation(6, 2), 30)
        self.assertEqual(permutation(10, 0), 1)

    # Test for combination function
    def test_combination(self):
        self.assertEqual(combination(5, 3), 10)
        self.assertEqual(combination(6, 2), 15)
        self.assertEqual(combination(10, 0), 1)

    # Test for absolute function
    def test_absolute(self):
        self.assertEqual(absolute(5), 5)
        self.assertEqual(absolute(-5), 5)
        self.assertEqual(absolute(0), 0)

    # Test for gcd function
    def test_gcd(self):
        self.assertEqual(gcd(24, 36), 12)
        self.assertEqual(gcd(7, 3), 1)
        self.assertEqual(gcd(56, 98), 14)

    # Test for lcm function
    def test_lcm(self):
        self.assertEqual(lcm(4, 5), 20)
        self.assertEqual(lcm(6, 8), 24)
        self.assertEqual(lcm(9, 12), 36)

if __name__ == '__main__':
    unittest.main()

