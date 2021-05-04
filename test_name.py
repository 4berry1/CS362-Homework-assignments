import unittest
import full_name

class testCaseAdd(unittest.TestCase):
    def test_name(self):
        self.assertEqual(full_name.fullname('joe', 'mama'), 'joe mama')
        self.assertEqual(full_name.fullname(8,10), '8 10')
    
    def test_name1(self):
        self.assertEqual(full_name.fullname('8','22' ), 30)

    def test_name2(self):
        self.assertEqual(full_name.fullname('26', 'smith'), '26 smith')

if __name__ == '__main__':
    unittest.main()