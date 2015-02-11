<<<<<<< HEAD
from TestVar import *
#from TestVarFactory import *
#from Solution import *
import unittest

testSuite = unittest.makeSuite(TestVar)
#testSuite.addTest(unittest.makeSuite(TestVar))
=======
from TestVar import * 
#from TestVarFactory import *
#from TestSolution import *
import unittest

testSuite = unittest.makeSuite(TestVar)
#testSuite.addTest(unittest.makeSuite(TestVarFactory))
>>>>>>> 307e71409dab197340644e39dd441029565579f6
#testSuite.addTest(unittest.makeSuite(TestSolution))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
