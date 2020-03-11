import unittest

from week5dp.money_change import moneychange
from week5dp.primitive_calculator import primitivecalculator

class Test_TestWeek5_DynamicPg1(unittest.TestCase):
      
    def test_get_change(self):
        expected = 2
        actual = moneychange.get_change(2)
        self.assertEqual(actual,  expected)
    
    def test_get_change2(self):
        expected = 9
        actual = moneychange.get_change(34)
        self.assertEqual(actual,  expected)
    
    def test_calculator(self):
        expected = [1,3,4,5]
        actual = list(primitivecalculator.calculate_dynamic(10))
        self.assertCountEqual(actual,expected)

    # def test_calculator2(self):
    #     expected = [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
    #     actual = list(primitivecalculator.calculate(96234))
    #     self.assertCountEqual(actual,expected)
    
    def test_calculator3(self):
        expected = [1]
        actual = list(primitivecalculator.calculate_dynamic(0))
        self.assertCountEqual(actual,expected)

    # def test_calculator4(self):
    #     expected = [1, 3, 9, 10]
    #     actual = list(primitivecalculator.calculate(10))
    #     self.assertCountEqual(actual,expected)

