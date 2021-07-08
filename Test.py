#This branch is for the unit test
#codes for the unittest will be uploaded after finishing the codes for the Calculator Logic 
import unittest
from Calculator05 import Genius_Pad
import math
class TestCalculator(unittest.TestCase):
    def test_addition(self):
        input=("1+1")
        result=eval(input)
        self.assertEqual(result,2)

    def test_subtraction(self):
        input=("5-9")
        result=eval(input)
        self.assertEqual(result,-4)

    def test_division(self):
        input=("10/5")
        result=eval(input)
        self.assertEqual(result,2)
    
    def test_multiplication(self):
        input=("9*8")
        result=eval(input)
        self.assertEqual(result,72)
    
    def test_exponent(self):
        result = math.pow(3,2)
        self.assertEqual(result,9)
       
    def test_squareroot(self):
        result= math.sqrt(25)
        self.assertEqual(result, 5)

    
if __name__=="__main__":
    unittest.main()
