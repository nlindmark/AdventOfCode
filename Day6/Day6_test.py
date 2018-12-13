import unittest
import Day6
class Test_TestDay6(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day6.solve("testdata1.txt"), 17)
    

    def test_puzzledata(self):
        self.assertEqual(Day6.solve("puzzledata.txt"), 3907)


if __name__ == '__main__':
    unittest.main()
     