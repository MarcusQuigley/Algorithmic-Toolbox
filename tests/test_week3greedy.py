import unittest

from week3greedy import moneychange
 

class Test_Week3_Greedy(unittest.TestCase):
      
    def test_money_change(self):
        expected = 2
        actual = moneychange.money_change(2)
        self.assertEqual(actual,  expected)
    
    def test_money_change2(self):
        expected = 6
        actual = moneychange.money_change(28)
        self.assertEqual(actual,  expected)
    
     