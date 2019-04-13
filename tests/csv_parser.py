import unittest
import china_stock_calendar.data as data

class testData(unittest.TestCase):

    def test_get(self):
        for item in data.holiday_set:
            print(item)