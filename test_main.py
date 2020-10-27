import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_arrayValues(self) : 
       for i in range(11) : 
          self.assertTrue( timesTable[i]==i*table, "One of more of the values in the timesTable array has not been set correctly" ) 
          
    def test_arrayLength(self) : 
       self.assertTrue( len(timesTable)==11, "The timesTable array has the wrong length" )
       
    def test_variableExists(self) : 
       self.assertTrue( "table" in globals(), "no variable called table has been defined in your program" )
       self.assertTrue( "timesTable" in globals(), "no variable called timesTable has been defined in your program" )
