import unittest
import Day8_2
class Test_TestDay8(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day8_2.solve("testdata1.txt"), 66)
    

    def test_puzzledata(self):
        self.assertEqual(Day8_2.solve("puzzledata.txt"), 42146)


if __name__ == '__main__':
    unittest.main()
     