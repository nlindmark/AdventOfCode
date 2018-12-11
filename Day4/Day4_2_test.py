import unittest
import Day4_2
class Test_TestDay4_2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day4_2.solve("testdata1.txt"), 4455)
    

    def test_puzzledata(self):
        self.assertEqual(Day4_2.solve("puzzledata.txt"), 49137)


if __name__ == '__main__':
    unittest.main()
     