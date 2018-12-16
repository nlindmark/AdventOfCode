import unittest
import Day9
class Test_TestDay8(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day9.solve("testdata1.txt"), 32)
    

    def test_puzzledata(self):
        self.assertEqual(Day9.solve("puzzledata.txt"), 428690)

    def test_puzzledata2(self):
        self.assertEqual(Day9.solve("puzzledata2.txt"), 3628143500)


if __name__ == '__main__':
    unittest.main()
     