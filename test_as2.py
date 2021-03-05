import unittest
from as2 import bmi, classification, retirement

class CalculationsTestCase(unittest.TestCase):

    def test_bmi(self):
                #inches pounds
        result = bmi(63,125)
                                #BMI
        self.assertEqual(result, 22.7)
    
    def test_classification(self):
                                #BMI
        result = classification(22.7)
                                #level of classification
        self.assertEqual(result, 1)

    def test_retirement(self):
                          #Salary  %saved S_Goal  Age
        result = retirement(100000, 0.15, 500000, 45)
                                #age that goal will be met
        self.assertEqual(result, 70)

unittest.main()