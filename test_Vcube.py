import unittest
import volume_of_cube

class testCaseAdd(unittest.TestCase):
    def test_cubev(self):
        self.assertEqual(volume_of_cube.cubev(10), 1000)
        self.assertEqual(volume_of_cube.cubev(-2), -8)
    
    def test_cubev1(self):
        self.assertEqual(volume_of_cube.cubev(7.46), 415.160936)

    def test_cubev2(self):
        self.assertEqual(volume_of_cube.cubev('error'), 0)

if __name__ == '__main__':
    unittest.main()