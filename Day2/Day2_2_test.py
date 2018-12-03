import unittest
import Day2_2
class Test_TestDay2_2(unittest.TestCase):
    def test_testdata1(self):
        self.assertEqual(Day2_2.solve("testdata1.txt"), "abcde")    

    def test_puzzledata(self):
        self.assertEqual(Day2_2.solve("puzzledata.txt"), "evsialkqyiurohzpwucngttmf")


if __name__ == '__main__':
    unittest.main()
     