import unittest
import Day3
class Test_TestDay3(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day3.solve("testdata1.txt"), 4)

    def test_puzzledata1(self):
        self.assertEqual(Day3.solve("puzzledata.txt"), 121163)


if __name__ == '__main__':
    unittest.main()
     