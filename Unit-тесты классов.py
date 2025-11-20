import unittest

class Calculator:
    def add(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multiply(a, b):
        return a * b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_minus(self):
        self.assertEqual(Calculator.minus(5, 3), 2)
        self.assertEqual(Calculator.minus(0, 5), -5)
        self.assertEqual(Calculator.minus(10, 10), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertEqual(Calculator.multiply(0, 5), 0)
        self.assertEqual(Calculator.multiply(-2, 4), -8)

unittest.main()