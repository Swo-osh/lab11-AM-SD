import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
         self.assertEqual(add(2, 3), 5)
         self.assertEqual(add(-1, 1), 0)
         self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
         self.assertEqual(subtract(5, 3), 2)
         self.assertEqual(subtract(-1, 1), -2)
         self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(15,mul(5,3))
        self.assertEqual(-1,mul(1,-1))
        self.assertEqual(-2,mul(2,-1))

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(5,div(4,20))
        with self.assertRaises(ZeroDivisionError):
            div(0,10)
        self.assertAlmostEqual(10,div(10,100))
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError, div, 0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(5, 25), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertRaises(ValueError, log, 10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion

        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(5,-2)
        with self.assertRaises(ValueError):
            logarithm(5,0)
        

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(5,hypotenuse(3,4))
        self.assertEqual(13,hypotenuse(5,12))
        self.assertEqual(17,hypotenuse(8,15))

    def test_sqrt(self): # 3 assertions
        
        with self.assertRaises(ValueError):
           square_root(-5)
        self.assertEqual(5,square_root(25))
        self.assertEqual(10,square_root(100))
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()