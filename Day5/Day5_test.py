import unittest
import Day5
class Test_TestDay4(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day5.solve("testdata1.txt"), 10)
    

    def test_puzzledata(self):
        self.assertEqual(Day5.solve("puzzledata.txt"), 10638)


if __name__ == '__main__':
    unittest.main()
     