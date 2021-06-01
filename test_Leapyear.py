import unittest
import Leapyear

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Leapyear.year(4), "4 is a leap year")
    def test_2(self):
        self.assertEqual(Leapyear.year(100), "100 is not a leap year")
    def test_3(self):
        self.assertEqual(Leapyear.year(400), "400 is a leap year")

if __name__ == '__main__':
    unittest.main()