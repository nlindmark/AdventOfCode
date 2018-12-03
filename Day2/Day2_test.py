import unittest
import Day2
class Test_TestDay2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day2.solve("testdata1.txt"), 12)    

    def test_puzzledata(self):
        self.assertEqual(Day2.solve("puzzledata.txt"), 6448)


if __name__ == '__main__':
    unittest.main()
     