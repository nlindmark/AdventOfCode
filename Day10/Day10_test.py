import unittest
import Day10
class Test_TestDay10(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day10.solve("testdata1.txt"), 3)
    

    def test_puzzledata(self):
        self.assertEqual(Day10.solve("puzzledata.txt"), 10136)


if __name__ == '__main__':
    unittest.main()
     