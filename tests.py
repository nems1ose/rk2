import unittest
from main import *


class rk2teste(unittest.TestCase):
    # Компьютеры
    autoparks = [Autopark(1, 'MacBook'), Autopark(2, 'RedmiBook'), Autopark(3, 'Imac'),
        Autopark(11, 'XiaomiBook'), Autopark(22, 'Ipad'), Autopark(33, 'PopicBook'),]

    # Микропроцессоры
    drivers = [Driver(1, 'Intel-i5' , 1998, 1), Driver(2, 'Intel-i7',  2010, 2), Driver(3, 'Intel-i9',  2021, 3),
               Driver(4, 'AMD-3',  2001, 3), Driver(5, 'AMD-6',  2004, 3),]

    goslings = [DriverInAutopark(1, 1), DriverInAutopark(2, 2), DriverInAutopark(3, 3), DriverInAutopark(3, 4), DriverInAutopark(3, 5),
                DriverInAutopark(11, 1), DriverInAutopark(22, 2), DriverInAutopark(33, 3), DriverInAutopark(33, 4), DriverInAutopark(33, 5),]


    def test_one(self):
        one_to_many_fq = [(park.name, driver.fio, driver.sal)
                          for park in autoparks
                          for driver in drivers
                          if park.id == driver.park_id]
        self.assertEqual(ans_one(one_to_many_fq),
                         ['MacBook', 'Intel-i5' , 1998])

    def test_two(self):
        one_to_many_fq = [(park.name, driver.fio, driver.sal)
                          for park in autoparks
                          for driver in drivers
                          if park.id == driver.park_id]
        self.assertEqual(ans_two(one_to_many_fq),
                         [('MacBook', 1998), ('RedmiBook', 2010), ('Imac', 2021)])

    def test_three(self):
        one_to_many_curr = [(park.name, dia.park_id, dia.driver_id)
                            for park in autoparks
                            for dia in goslings
                            if park.id == dia.park_id]
        many_to_many_ans = [(park_name, d.fio)
                            for park_name, park_id, driver_id in one_to_many_curr
                            for d in drivers if d.id == driver_id]
        self.assertEqual(ans_three(many_to_many_ans),
                         {'MacBook': ['Intel-i5'],
                          'RedmiBook': ['Intel-i7'],
                          'Imac': ['Intel-i9', 'AMD-3', 'AMD-6'],
                          'XiaomiBook': ['Intel-i5'], 'Ipad': ['Intel-i7'],
                          'PopicBook': ['Intel-i9', 'AMD-3', 'AMD-6']})


if __name__ == '__main__':
    unittest.main()
