import unittest
import Day3_2
class Test_TestDay3_2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day3_2.solve("testdata1.txt"), '3')

    def test_puzzledata1(self):
        self.assertEqual(Day3_2.solve("puzzledata.txt"), '943')


if __name__ == '__main__':
    unittest.main()
     