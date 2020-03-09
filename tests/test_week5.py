import unittest
from Week5 import MoneyChange
from Week5 import PrimitiveCalculator

class Test_TestWeek5_DynamicPg1(unittest.TestCase):
    def test_get_change(self):
        expected = 2
        actual = MoneyChange.get_change(2)
        self.assertEqual(actual,  expected)
    
    def test_get_change2(self):
        expected = 9
        actual = MoneyChange.get_change(34)
        self.assertEqual(actual,  expected)
    
    def test_calculator(self):
        expected = [1,3,4,5]
        actual = list(PrimitiveCalculator.calculate(5))
        self.assertCountEqual(actual,expected)

    def test_calculator2(self):
        expected = [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
        actual = list(PrimitiveCalculator.calculate(96234))
        self.assertCountEqual(actual,expected)
    
    def test_calculator3(self):
        expected = [1]
        actual = list(PrimitiveCalculator.calculate(0))
        self.assertCountEqual(actual,expected)

    def test_calculator4(self):
        expected = [1, 3, 9, 10]
        actual = list(PrimitiveCalculator.calculate(10))
        self.assertCountEqual(actual,expected)

