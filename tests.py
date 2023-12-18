import unittest
from main import *


class rk2teste(unittest.TestCase):
    # Компьютеры
computers = [   Computer(1, 'MacBook'), Computer(2, 'RedmiBook'), Computer(3, 'Imac'),
                Computer(11, 'XiaomiBook'), Computer(22, 'Ipad'), Computer(33, 'PopicBook'),]
# Микропроцессоры
drivers = [ Driver(1, 'Intel-i5' , 1998, 1), Driver(2, 'Intel-i7',  2010, 2),
            Driver(3, 'Intel-i9',  2021, 3), Driver(4, 'AMD-3',  2001, 3), Driver(5, 'AMD-6',  2004, 3),]

goslings = [    DriverInComputer(1, 1), DriverInComputer(2, 2), DriverInComputer(3, 3), DriverInComputer(3, 4), DriverInComputer(3, 5),
                DriverInComputer(11, 1), DriverInComputer(22, 2), DriverInComputer(33, 3), DriverInComputer(33, 4), DriverInComputer(33, 5),]


    def test_one(self):
        one_to_many_fq = [(park.name, driver.fio, driver.sal)
                          for park in autoparks
                          for driver in drivers
                          if park.id == driver.park_id]
        self.assertEqual(ans_one(one_to_many_fq),
                         ['Астафьево', 'Георгич 25000'])

    def test_two(self):
        one_to_many_fq = [(park.name, driver.fio, driver.sal)
                          for park in autoparks
                          for driver in drivers
                          if park.id == driver.park_id]
        self.assertEqual(ans_two(one_to_many_fq),
                         [('Астафьево', 25000), ('Рязанский ЦАВ', 35000), ('Щёлковский АВ', 45000)])

    def test_three(self):
        one_to_many_curr = [(park.name, dia.park_id, dia.driver_id)
                            for park in autoparks
                            for dia in goslings
                            if park.id == dia.park_id]
        many_to_many_ans = [(park_name, d.fio)
                            for park_name, park_id, driver_id in one_to_many_curr
                            for d in drivers if d.id == driver_id]
        self.assertEqual(ans_three(many_to_many_ans),
                         {'Астафьево': ['Георгич'],
                          'Рязанский ЦАВ': ['Дмитрич'],
                          'Щёлковский АВ': ['Геннадич', 'Палыч', 'Михалыч'],
                          'Котельники': ['Георгич'], 'Рязань-2': ['Дмитрич'],
                          'Щёлково': ['Геннадич', 'Палыч', 'Михалыч']})


if __name__ == '__main__':
    unittest.main()
