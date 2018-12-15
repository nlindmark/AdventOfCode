import unittest
import Day7
class Test_TestDay7(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day7.solve("testdata1.txt",2), 258)
    

    def test_puzzledata(self):
        self.assertEqual(Day7.solve("puzzledata.txt",5), 985)


if __name__ == '__main__':
    unittest.main()
     