import unittest

from week3greedy import moneychange
from week3greedy import maxlootvalue
from week3greedy import maxadrevenue
from week3greedy import collecting_signatures

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

    def test_max_ad_revenue(self):
        ads = [23]
        revenue = [39]        
        expected = 897
        actual = maxadrevenue.max_add_revenue(ads, revenue)
        self.assertEqual(actual,  expected)

    def test_max_ad_revenue2(self):
        ads = [1,-5,3]
        revenue = [1,4,-2]        
        expected = 23
        actual = maxadrevenue.max_add_revenue(ads, revenue)
        self.assertEqual(actual,  expected)

    def test_signatures(self):
        start_times = [1,3,2]
        end_times = [3, 6, 5]
        n = len(start_times)
        expected = 1
        points = [3]
        segments = [None] * n
        for i in range(n):
            segments[i] = collecting_signatures.Segment(start_times[i], end_times[i])

        actual = collecting_signatures.signatures(segments)
        self.assertEqual(len(actual),  expected)
        self.assertListEqual(points, actual)

    def test_signatures2(self):
        start_times = [4,1,2, 5]
        end_times = [7,3,5,6]
        n = len(start_times)
        expected = 2
        points = [3,6]
        segments = [None] * n
        for i in range(n):
            segments[i] = collecting_signatures.Segment(start_times[i], end_times[i])

        actual = collecting_signatures.signatures(segments)
        self.assertEqual(len(actual),  expected)
        self.assertListEqual(points, actual)

     