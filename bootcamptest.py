import unittest

import calc

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.calculate(12,4,'add'), 16)

    def test_substraction(self):
        self.assertEqual(calc.calculate(12,4,'substract'), 8)

    def test_multiplication(self):
        self.assertEqual(calc.calculate(12,4,'multiply'), 48)

    def test_division(self):
        self.assertEqual(calc.calculate(12,4,'divide'), 3)
    def test_greater(self):
	self.assertEqual(calc.calculate(12,4,'greater'), 12)
    def test_smaller(self):
        self.assertEqual(calc.calculate(12,4,'smaller'), 4)
    def test_modulus(self):
        self.assertEqual(calc.calculate(12,4,'modulus'), 0)
    def test_boolean(self):
        self.assertEqual(calc.calculate(12,4,'boolean'), False)
    def test_equal(self):
        self.assertEqual(calc.calculate(12,4,'equal'), "Not Equal")
    def test_append(self):
        self.assertEqual(calc.calculate(12,4,'append'), 124)

if __name__ == '__main__':

	unittest.main()
