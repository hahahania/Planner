import unittest
from doplikucsv import new_info, acsending_date, decsending_date, decsending_update_date, acsending_update_date
import csv
import os


class TestDoplikucsv(unittest.TestCase):
    def setUp(self):
        self.test_file = open('test_file.csv')
        self.line1 = ['urodziny mamy', '2023-12-20', '18: 45', 'NO', '87',
                      'Zdrowie', '', '2023-01-08', '07:15', '2023-01-08', '07:15']

        self.line2 = ['Urodziny', '2023-05-22', '19:00',
                      'NI', '60', 'Znajomi', '', '2023-01-06', '09:40', '2023-01-06', '09:40']
        self.line3 = ['Lekarz', '2023-04-30', '13:00', 'WY',
                      '10', 'Zdrowie', 'Przed zrobić badanie krwi', '2022-12-31', '21:15', '2022-12-31', '21:15']

    def tearDown(self):
        self.test_file.close()

    def test_new_info(self):
        new_info(self.line1, 'test_file.csv')
        new_info(self.line2, 'test_file.csv')
        new_info(self.line3, 'test_file.csv')
        self.testdata = list(csv.reader(self.test_file))
        self.assertIn(self.line1, self.testdata)
        self.assertIn(self.line2, self.testdata)
        self.assertIn(self.line3, self.testdata)

    # test data realizacji malejąco
    def test_ascending_date(self):
        acsending_date('test_file.csv')
        self.testdata = list(csv.reader(self.test_file))
        self.assertEqual(self.testdata[0], self.line3)

    # test data malejąco realizacji
    def test_descending_date(self):
        decsending_date('test_file.csv')
        self.testdata = list(csv.reader(self.test_file))
        self.assertEqual(self.testdata[0], self.line3)

    # test data aktualizacji rosnąco
    def test_update_ascending_date(self):
        acsending_update_date('test_file.csv')
        self.testdata = list(csv.reader(self.test_file))
        self.assertEqual(self.testdata[0], self.line3)

    # test data aktualizacji malejąco
    def test_update_descending_date(self):
        decsending_update_date('test_file.csv')
        self.testdata = list(csv.reader(self.test_file))
        self.assertEqual(self.testdata[0], self.line3)


if __name__ == '__main__':
    unittest.main()
