import unittest
import FizzBuzz

class testCaseAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(FizzBuzz.fizzbuzz(3), "Fizz")
    def test_2(self):
        self.assertEqual(FizzBuzz.fizzbuzz(5), "Buzz")
    def test_3(self):
        self.assertEqual(FizzBuzz.fizzbuzz(15), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()