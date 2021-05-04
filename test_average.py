import unittest
import average_list

class testCaseAdd(unittest.TestCase):
    def test_cubev(self):
        self.assertEqual(average_list.average([1,2,3,4,5,6,7,8,9,10,11]), 6)
        self.assertEqual(average_list.average([]), 0)
    
    def test_cubev1(self):
        self.assertEqual(average_list.average([1,'two',3,4,5]), 3)

    def test_cubev2(self):
        self.assertEqual(average_list.average([-1,2,-3,4,-5,6,-7,8]), .5)

if __name__ == '__main__':
    unittest.main()