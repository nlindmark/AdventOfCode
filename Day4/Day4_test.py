import unittest
import Day4
class Test_TestDay4(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day4.solve("testdata1.txt"), 240)
    

    def test_puzzledata(self):
        self.assertEqual(Day4.solve("puzzledata.txt"), 72925)


if __name__ == '__main__':
    unittest.main()
     