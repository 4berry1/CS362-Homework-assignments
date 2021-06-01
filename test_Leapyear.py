import unittest
import Leapyear

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Leapyear.year(4), "4 is a leap year")


if __name__ == '__main__':
    unittest.main()