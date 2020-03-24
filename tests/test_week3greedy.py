import unittest

from week3greedy import moneychange
from week3greedy import maxlootvalue

class Test_Week3_Greedy(unittest.TestCase):
      
    def test_money_change(self):
        expected = 2
        actual = moneychange.money_change(2)
        self.assertEqual(actual,  expected)
    
    def test_money_change2(self):
        expected = 6
        actual = moneychange.money_change(28)
        self.assertEqual(actual,  expected)

    def test_max_value_of_loot(self):
        weights = [60,100,120]
        values = [20,50,30]        
        capacity = 50
        expected = 180
        actual = maxlootvalue.max_value_of_loot(capacity, weights, values)
        self.assertEqual(actual,  expected)

    def test_max_value_of_loot2(self):
        weights = [500]
        values = [30]        
        capacity = 10
        expected = 166.6667
        actual = maxlootvalue.max_value_of_loot(capacity, weights, values)
        self.assertEqual(actual,  expected)
    
     