# this file will have our tests written

# importing our class and testing modules
from simple_calc import Simple_Calc
import unittest
import pytest

# let's create a class to run our tests

class Calctest(unittest.TestCase):
# unittest.TestCase works with unittest frame work as parent class

# instantiating our calculator class so we can access its methods
    calc = Simple_Calc()

# IMPORTANT - we MUST use test word in our functions so python interpretor knows what are we testing

    def test_add(self):
# self.assertEqual(self.calc.add(2,4), 6)
        self.assertEqual(self.calc.add(2,4), 6)
# what are we asking python to test for us
# we are asking python to test / check if 2 + 4 = 6 if True pass if False fail the test
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,2), 2)
# Boolean tests if 4-2 returns 2, then passes / fails accordingly
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,4), 16)
        
    def test_devide(self):
        self.assertEqual(self.calc.devide(10,2), 5)