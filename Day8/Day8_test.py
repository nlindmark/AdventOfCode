import unittest
import Day8
class Test_TestDay8(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day8.solve("testdata1.txt"), 138)
    

    def test_puzzledata(self):
        self.assertEqual(Day8.solve("puzzledata.txt"), 42146)


if __name__ == '__main__':
    unittest.main()
     