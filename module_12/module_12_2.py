'''
Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90. У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results. В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка. В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
'''

import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = runner_and_tournament.Runner('Усэйн', 10)
        self.run2 = runner_and_tournament.Runner('Андрей', 9)
        self.run3 = runner_and_tournament.Runner('Ник', 3)
        self.run4 = runner_and_tournament.Runner('Алекс', 5)

    @classmethod
    def tearDownClass(cls):
        result = {}
        for testkey, testval in cls.all_results.items():
            print(f'TEST: {testkey}')
            for key, val in testval.items():
                result[key] = str(val.name)
            print(result)

    def testrun_1(self):
        run_1 = runner_and_tournament.Tournament(90, self.run1, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish

    def testrun_2(self):
        run_1 = runner_and_tournament.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish

    def testrun_3(self):
        run_1 = runner_and_tournament.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish

if __name__ == "__main__":
    unittest.main()
