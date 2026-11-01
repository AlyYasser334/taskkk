import main
import unittest



class testingfunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(main.add_function(2,3),5)
    def test2(self):
        self.assertEqual(main.add_function(2,-3),-1)