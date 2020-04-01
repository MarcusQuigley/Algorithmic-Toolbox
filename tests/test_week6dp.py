import unittest

from week6dp import maxgold
from week6dp import knapsack

class Test_TestWeek6_DynamicPg2(unittest.TestCase):
      
    def test_get_change(self):
        expected = 2
        actual = 3# maxgold.get_change(2)
        self.assertEqual(actual,  expected)
    
    def test_knapsack_with_repetitions(self):
        capacity = 10
        values  = (30,14,16,9)
        weights= (6,3,4,2)
        expected = 48
        actual = knapsack.knapsack_with_repetitions(capacity, weights, values)
        self.assertEqual(actual, expected)

    def test_knapsack_recursive_with_repetitions(self):
        capacity = 10
        values  = (30,14,16,9)
        weights= (6,3,4,2)
        expected = 48
        actual =22
        knapsack.knapsack_recursive_with_repetitions_stpete(capacity, weights, values)
        self.assertEqual(actual, expected)
    
    def test_knapsack_without_repetitions_stpete(self):
        capacity = 10
        values  = (30,14,16,9)
        weights= (6,3,4,2)
        expected = 46
        actual = knapsack.knapsack_without_repetitions_stpete(weights, values,capacity)
        self.assertEquals(actual, expected)
    
    def test_max_gold(self):
        capacity = 10
        weights = (1,4,8)
        expected = 9
        actual = maxgold.max_gold(capacity,weights)
        self.assertEqual(expected, actual)