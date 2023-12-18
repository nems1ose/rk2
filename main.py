""""
1)«Отдел» и «Сотрудник» связаны соотношением один-ко-многим.
 Выведите список всех отделов, у которых название начинается с буквы «А», и список работающих
  в них сотрудников.
2)«Отдел» и «Сотрудник» связаны соотношением один-ко-многим.
Выведите список отделов с максимальной зарплатой сотрудников в каждом отделе,
 отсортированный по максимальной зарплате.
3)«Отдел» и «Сотрудник» связаны соотношением многие-ко-многим.
Выведите список всех связанных сотрудников и отделов, отсортированный по отделам,
сортировка по сотрудникам произвольная.
7 Вариант (Микропроцессор, Компьютер)
"""

from operator import itemgetter


class Driver:
    """Микропроцессор"""
    def __init__(self, id, fio, sal, park_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.park_id = park_id


class Autopark:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DriverInAutopark:
    """
    'Микропроцессоры' для реализации
    связи многие-ко-многим
    """
    def __init__(self, park_id, emp_id):
        self.park_id = park_id
        self.driver_id = emp_id


# Компьютеры
autoparks = [
    Autopark(1, 'MacBook'), Autopark(2, 'RedmiBook'), Autopark(3, 'Imac'),
    Autopark(11, 'XiaomiBook'), Autopark(22, 'Ipad'), Autopark(33, 'PopicBook'),]

# Микропроцессоры
drivers = [Driver(1, 'Intel-i5' , 1998, 1), Driver(2, 'Intel-i7',  2010, 2), Driver(3, 'Intel-i9',  2021, 3),
           Driver(4, 'AMD-3',  2001, 3), Driver(5, 'AMD-6',  2004, 3),]

goslings = [DriverInAutopark(1, 1), DriverInAutopark(2, 2), DriverInAutopark(3, 3), DriverInAutopark(3, 4), DriverInAutopark(3, 5),
DriverInAutopark(11, 1), DriverInAutopark(22, 2), DriverInAutopark(33, 3), DriverInAutopark(33, 4), DriverInAutopark(33, 5),]

def ans_one(one_to_many_fq):
    print("First Question")
    sorted(one_to_many_fq, key=itemgetter(0))
    i = 0
    j = 0
    ans = []
    """Sliding windows"""
    while i < len(one_to_many_fq) and one_to_many_fq[i][0].startswith('M'):
        if i == j:
            ans.append(one_to_many_fq[j][0])
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            ans.append(one_to_many_fq[j][1] + ' ' + str(one_to_many_fq[j][2]))
            j += 1
        i = j
    return ans


def ans_two(one_to_many_fq):
    print("Second Question")
    sorted(one_to_many_fq, key=itemgetter(0, 2))
    i = 0
    j = 0
    parks_maximus = []
    ans = []
    """Sliding windows"""
    while i < len(one_to_many_fq):
        curr = 0
        while j < len(one_to_many_fq) and one_to_many_fq[j][0] == one_to_many_fq[i][0]:
            if one_to_many_fq[j][2] > curr:
                curr = one_to_many_fq[j][2]
            j += 1
        parks_maximus.append((one_to_many_fq[i][0], curr))
        i = j
    for e in parks_maximus:
        ans.append(e)
    return ans


def ans_three(many_to_many_ans):
    print("Third Question")
    sorted(many_to_many_ans, key=itemgetter(0, 1))
    ans = dict()
    i = 0
    j = 0
    while i < len(many_to_many_ans) and j < len(many_to_many_ans):
        ans[many_to_many_ans[i][0]] = []
        while j < len(many_to_many_ans) and many_to_many_ans[j][0] == many_to_many_ans[i][0]:
            ans[many_to_many_ans[i][0]].append(many_to_many_ans[j][1])
            j += 1
        i = j
    return ans


def main():
    # Соединение данных один-ко-многим
    one_to_many_fq = [(park.name, driver.fio, driver.sal)
                      for park in autoparks
                      for driver in drivers
                      if park.id == driver.park_id]
    # Соединение данных один-ко-многим
    one_to_many_curr = [(park.name, dia.park_id, dia.driver_id)
                        for park in autoparks
                        for dia in goslings
                        if park.id == dia.park_id]

    many_to_many_ans = [(park_name, d.fio)
                        for park_name, park_id, driver_id in one_to_many_curr
                        for d in drivers if d.id == driver_id]

    print(ans_one(one_to_many_fq))
    print(ans_two(one_to_many_fq))
    print(ans_three(many_to_many_ans))


if __name__ == '__main__':
    main()
