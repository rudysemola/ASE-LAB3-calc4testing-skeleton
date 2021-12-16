from calc.calculator import calculator as c
import unittest

# TODO: Extend these unit tests for the calculator module!


class TestAdd(unittest.TestCase):
    def test_add_integers_positive(self):
        result = c.sum(1, 2)
        self.assertEqual(result, 3)

    def test_add_integers_negative(self):
        result = c.sum(-1, -2)
        self.assertEqual(result, -3)

    def test_add_integers_pos_neg(self):
        result = c.sum(1, -2)
        self.assertEqual(result, -1)

    def test_add_integers_neg_pos(self):
        result = c.sum(-1, 2)
        self.assertEqual(result, 1)

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)

    "RS test"
    def test_multiply_integers_positive(self):
        result = c.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_multiply_integers_negative(self):
        result = c.multiply(-5, -10)
        self.assertEqual(result, 50)
    
    def test_multiply_integers_pos_neg(self):
        result = c.multiply(2, -10)
        self.assertEqual(result, -20)

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-2, 10)
        self.assertEqual(result, -20)

    def test_multiply_integers_zero(self):
        result1 = c.multiply(-2, 0)
        self.assertEqual(result1, 0)
        result2 = c.multiply(0, 2)
        self.assertEqual(result2, 0)

    def test_subtract_integers_positive(self):
        result = c.subtract(10, 6)
        self.assertEqual(result, 4)

    def test_subtract_integers_negative(self):
        result = c.subtract(2, 5)
        self.assertEqual(result, -3)


if __name__ == "__main__":
    unittest.main()
