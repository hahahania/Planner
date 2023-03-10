import unittest
from wydarzenie import Event
from datetime import datetime


class TestWydarzenie(unittest.TestCase):

    def setUp(self):

        self.event1 = Event('Urodziny', '2023-05-22', '19:00',
                            'NI', '60', 'Znajomi', '')
        self.event2 = Event('Lekarz', '2023-04-30', '13:00', 'WY',
                            '10', 'Zdrowie', 'Przed zrobić badanie krwi')

    def test_str(self):

        self.assertEqual(self.event1.__str__(
        ), 'Nazwa wydarzenia : Urodziny\nData wydarzenia : 2023-05-22\nGodzina : 19:00\nPriorytet : NI\nStopień wykonania : 60\nKategoria : Znajomi\nOpis : ')
        self.assertEqual(self.event2.__str__(
        ), 'Nazwa wydarzenia : Lekarz\nData wydarzenia : 2023-04-30\nGodzina : 13:00\nPriorytet : WY\nStopień wykonania : 10\nKategoria : Zdrowie\nOpis : Przed zrobić badanie krwi')

    def test_creating_list(self):
        self.assertEqual(self.event1.creating_list(), ['Urodziny', '2023-05-22', '19:00',
                                                       'NI', '60', 'Znajomi', '', datetime.today().strftime('%Y-%m-%d'), datetime.now().strftime("%H:%M"), None, None])
        self.assertEqual(self.event2.creating_list(), ['Lekarz', '2023-04-30', '13:00', 'WY',
                                                       '10', 'Zdrowie', 'Przed zrobić badanie krwi', datetime.today().strftime('%Y-%m-%d'), datetime.now().strftime("%H:%M"), None, None])

    def test_update(self):
        self.event1.update()
        self.event2.update()

        self.assertEqual(self.event1.update_date,
                         datetime.today().strftime('%Y-%m-%d'))
        self.assertEqual(self.event1.update_time,
                         datetime.today().strftime('%H:%M'))
        self.assertEqual(self.event2.update_date,
                         datetime.today().strftime('%Y-%m-%d'))
        self.assertEqual(self.event2.update_time,
                         datetime.today().strftime('%H:%M'))


if __name__ == '__main__':
    unittest.main()
