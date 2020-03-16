import unittest

from week5dp.money_change import moneychange
from week5dp.primitive_calculator import primitivecalculator
from week5dp.edit_distance import edit_distance
from week5dp.lcs_of_two import lcs_of_two

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

    def test_minimum_edit_distance(self):
        str1 = "abcfg"
        str2 = "adceg"
        expected = 2
        actual = edit_distance.minimum_edit_distance(str1, str2)
        self.assertEqual(actual, expected)

    def test_minimum_edit_distance2(self):
        str1 = "ab"
        str2 = "ab"
        expected = 0
        actual = edit_distance.minimum_edit_distance(str1, str2)
        self.assertEqual(actual, expected)

    def test_minimum_edit_distance3(self):
        str1 = "short"
        str2 = "ports"
        expected = 3
        actual = edit_distance.minimum_edit_distance(str1, str2)
        self.assertEqual(actual, expected)

    def test_minimum_edit_distance4(self):
        str1 = "editing"
        str2 = "distance"
        expected = 5
        actual = edit_distance.minimum_edit_distance(str1, str2)
        self.assertEqual(actual, expected)

    def test_lcs_of_two(self):
        str1 = "275"
        str2 = "25"
        expected = 2
        actual = lcs_of_two.lcs_of_two(str1, str2)
        self.assertEqual(actual, expected)

    def test_lcs_of_two1(self):
        str1 = "7"
        str2 = "1234"
        expected = 0
        actual = lcs_of_two.lcs_of_two(str1, str2)
        self.assertEqual(actual, expected)

    def test_lcs_of_two2(self):
        str1 = "2783"
        str2 = "5287"
        expected = 2
        actual = lcs_of_two.lcs_of_two(str1, str2)
        self.assertEqual(actual, expected)