import unittest
import module_12_3

athleticsTS = unittest.TestSuite()
athleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.Runner_test))
athleticsTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(athleticsTS)