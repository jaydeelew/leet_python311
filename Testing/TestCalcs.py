import unittest
from Calcs import Calculations


class TestThis(unittest.TestCase):
    def setUp(self):
        self.calculation = Calculations(8, 2)

    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, "The sum is wrong.")

    def test_product(self):
        self.assertEqual(self.calculation.get_product(), 16, "The product is wrong.")

    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, "The quotient is wrong.")


if __name__ == "__main__":
    unittest.main()
