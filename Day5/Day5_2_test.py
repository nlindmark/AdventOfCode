import unittest
import Day5_2
class Test_TestDay5_2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day5_2.solve("testdata1.txt"), 4)
    

    def test_puzzledata(self):
        self.assertEqual(Day5_2.solve("puzzledata.txt"), 4944)


if __name__ == '__main__':
    unittest.main()
     