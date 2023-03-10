import unittest
from poprawność import check_date, check_time


class TestPoprawnosc(unittest.TestCase):
    def setUp(self):
        self.time1 = '12.20'
        self.time2 = '12:20'
        self.date1 = '01-01-2023'
        self.date2 = '2023-01-01'

    def test_check_date(self):
        self.assertTrue(check_time(self.time2))
        self.assertEqual(check_time(self.time1), None)

    def test_check_time(self):
        self.assertTrue(check_date(self.date2))
        self.assertEqual(check_date(self.date1), None)


if __name__ == '__main__':
    unittest.main()
