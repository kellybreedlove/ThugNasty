from TestAdder import * #this syntax imports whatever is defined in TestAdder into the current namespace
from TestTimes import *
import unittest

testSuite = unittest.makeSuite(TestAdder)
testSuite.addTest(unittest.makeSuite(TestTimes))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
