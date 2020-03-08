import unittest
from Week5 import MoneyChange

class Test_TestWeek5_DynamicPg1(unittest.TestCase):
    def test_get_change(self):
        self.assertEqual(MoneyChange.get_change(5),  "you have 5")

