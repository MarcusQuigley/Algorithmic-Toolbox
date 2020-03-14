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
        total = 5
        ops =  primitivecalculator.min_operations(total)
        actual = primitivecalculator.operations_list(ops, total)
        self.assertCountEqual(actual,expected)

    def test_calculator2(self):
        expected = [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
        total = 96234
        ops =  primitivecalculator.min_operations(total)
        actual = primitivecalculator.operations_list(ops, total)
        self.assertCountEqual(actual,expected)
    
    def test_calculator3(self):
        expected = [1]
        total = 1
        ops =  primitivecalculator.min_operations(total)
        actual = primitivecalculator.operations_list(ops, total)
        self.assertCountEqual(actual,expected)

    def test_calculator4(self):
        expected = [1, 3, 9, 10]
        total = 10
        ops =  primitivecalculator.min_operations(total)
        actual = primitivecalculator.operations_list(ops, total)
        self.assertCountEqual(actual,expected)

