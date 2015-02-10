#from TestVar import *
from TestVarFactory import *
#from Solution import *
import unittest

testSuite = unittest.makeSuite(TestVarFactory)
#testSuite.addTest(unittest.makeSuite(TestVar))
#testSuite.addTest(unittest.makeSuite(TestSolution))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
