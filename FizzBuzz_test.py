import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(FizzBuzz.fizzbuzz(3), "Fizz")



if __name__ == '__main__':
    unittest.main()