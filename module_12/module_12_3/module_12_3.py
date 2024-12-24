import unittest
import runner_and_tournament, runner


class Runner_test(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walk = runner.Runner('Test1')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner.Runner('Test2')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk = runner.Runner('Test1')
        run = runner.Runner('Test2')
        for i in range(10):
            walk.walk()
            run.run()
            self.assertNotEqual(run.distance, walk.distance)


class TournamentTest(unittest.TestCase):
    all_results = None
    is_frozen = True

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
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_1(self):
        run_1 = runner_and_tournament.Tournament(90, self.run1, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1} и {self.run3}'] = finish
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_2(self):
        run_1 = runner_and_tournament.Tournament(90, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run2} и {self.run3}'] = finish
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testrun_3(self):
        run_1 = runner_and_tournament.Tournament(90, self.run1, self.run2, self.run3)
        finish = run_1.start()
        self.assertTrue(list(finish.values())[-1].name == str(self.run3))
        self.all_results[f'Результат {self.run1}, {self.run2} и {self.run3}'] = finish

if __name__ == "__main__":
    unittest.main()
