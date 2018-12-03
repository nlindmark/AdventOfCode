import unittest
import Day1
class Test_TestDay1(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day1.solve("testdata1.txt"), 3)
    
    def test_testdata2(self):
        self.assertEqual(Day1.solve("testdata2.txt"), 0)
    
    def test_testdata3(self):
        self.assertEqual(Day1.solve("testdata3.txt"), -6)

    def test_puzzledata(self):
        self.assertEqual(Day1.solve("puzzledata.txt"), 490)


if __name__ == '__main__':
    unittest.main()
     