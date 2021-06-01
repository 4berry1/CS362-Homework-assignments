import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(FizzBuzz.main(), 0)



if __name__ == '__main__':
    unittest.main()