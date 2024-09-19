# Homework 6 - UnitTest
# This program uses unittest.TestCase methods to confirm that the addition and 
# subtraction of date and timedelta objects produce correct results.
# CS 231 - Advanced Python


import unittest
from datetime import date, timedelta


class TestDateTimedeltaOperations(unittest.TestCase):

    def setUp(self):
        self.sample_date = date(2023, 10, 15)
        self.sample_timedelta = timedelta(days=200)
        self.added_date = self.sample_date + self.sample_timedelta

    def test_date_plus_timedelta(self):
        result = self.sample_date + self.sample_timedelta
        self.assertEqual(result, self.added_date)

    def test_date_minus_date(self):
        result = self.added_date - self.sample_date
        self.assertEqual(result, self.sample_timedelta)

    def test_date_minus_timedelta(self):
        result = self.added_date - self.sample_timedelta
        self.assertEqual(result, self.sample_date)

    def test_random_date_addition(self):
        d = date(2019, 7, 15)
        delta = timedelta(days=20)
        result = d + delta
        self.assertEqual(result, date(2019, 8, 4))


if __name__ == "__main__":
    unittest.main()
