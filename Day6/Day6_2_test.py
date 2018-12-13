import unittest
import Day6_2
class Test_TestDay6_2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day6_2.solve("testdata1.txt",32), 16)
    

    def test_puzzledata(self):
        self.assertEqual(Day6_2.solve("puzzledata.txt",10000), 42036)


if __name__ == '__main__':
    unittest.main()
     