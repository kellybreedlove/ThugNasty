from VarFactory import *
from LinearTerm import *
import unittest

class TestVarFactory(unittest.TestCase):
	
	#"""Test VarFactory.py's testVar() method"""
 	def testTestVar(self):
		factory = VarFactory()
		a = factory.testVar("Billy Joe", HGRAD)
		b = factory.testVar("Liam", HGRAD)
		self.assertEqual(a.getName(), "Billy Joe")
		self.assertEqual(a.getSpace(), HGRAD) 
		self.assertNotEqual(a.ID(), b.ID()) #different IDs

	#"""Test VarFactory.py's FieldVar() method"""
 	def testFieldVar(self):
		factory = VarFactory()
		a = factory.fieldVar("Crowe")
		b = factory.fieldVar("Liam")
		self.assertEqual(a.getName(), "Crowe")#check name
		self.assertNotEqual(a.ID(), b.ID()) #different IDs

	#"""Test VarFactory.py's fluxVar() method"""
 	def testFluxVar(self):
		factory = VarFactory()
		lt = LinearTerm()
		a = factory.fluxVar("Crowe", lt)
		b = factory.fluxVar("Liam", lt)
		self.assertEqual(a.getName(), "Crowe")#check name
		self.assertNotEqual(a.ID(), b.ID()) #different IDs

	#"""Test VarFactory.py's traceVar() method"""
 	def testTraceVar(self):
		factory = VarFactory()
		lt = LinearTerm()
		a = factory.traceVar("Crowe", lt)
		b = factory.traceVar("Liam", lt)
		self.assertEqual(a.getName(), "Crowe")#check name
		self.assertNotEqual(a.ID(), b.ID()) #different IDs

	def testTraceVar(self):
		factory = VarFactory()
		a = factory.traceVar("Crowe", HGRAD)
		b = factory.traceVar("Liam", HGRAD)
		self.assertEqual(a.getName(), "Crowe")#check name
		self.assertNotEqual(a.ID(), b.ID()) #different IDs
		self.assertEqual(a.getSpace(), HGRAD)
	
	#"""Test VarFactory.py's test() method"""
	def testTest(self):
		factory = VarFactory()
		a = factory.testVar("Billy Joe", HGRAD)
		b = test(a.ID())
		self.assertEqual(b.getName(), a.getName())
		self.assertEqual(b.getSpace(), a.getSpace())
		
  #"""Test VarFactory.py's trial() method"""
	def testTrial(self):
		factory = VarFactory()
		a = factory.fieldVar("Billy Joe", HGRAD)
		b = test(a.ID())
		self.assertEqual(b.getName(), a.getName())
		self.assertEqual(b.getSpace(), a.getSpace())

	#"""Test VarFactory.py's testIDs() method"""
	def testTestIDs(self):
		factory = VarFactory()
		a = factory.testVar("Liam", HGRAD)
		b = factory.testVar("Crowe", HGRAD)
		c = factory.testVar("Noris", HGRAD)
		array = factory.testIDs()
		self.assertEqual(array[0].ID(), a.ID())
		self.assertEqual(array[1].ID(), b.ID())
		self.assertEqual(array[2].ID(), c.ID())

	#"""Test VarFactory.py's trialIDs() method"""
	def testTrialIDs(self):
		factory = VarFactory()
		a = factory.fieldVar("Liam", HGRAD)
		b = factory.fieldVar("Crowe", HGRAD)
		c = factory.fieldVar("Noris", HGRAD)
		array = factory.trialIDs()
		self.assertEqual(array[0].ID(), a.ID())
		self.assertEqual(array[1].ID(), b.ID())
		self.assertEqual(array[2].ID(), c.ID())

	#"""Test VarFactory.py's fieldVars() method"""
	def testFieldIDs(self):
		factory = VarFactory()
		a = factory.fieldVar("Liam", HGRAD)
		b = factory.fieldVar("Crowe", HGRAD)
		c = factory.fieldVar("Noris", HGRAD)
		array = factory.fieldVars()
		self.assertEqual(array[0].getName(), a.getName())
		self.assertEqual(array[1].getName(), b.getName())
		self.assertEqual(array[2].getName(), c.getName())

	#"""Test VarFactory.py's fluxVars() method"""
	def testFluxIDs(self):
		factory = VarFactory()
		a = factory.fluxVar("Liam", HGRAD)
		b = factory.fluxVar("Crowe", HGRAD)
		c = factory.fluxVar("Noris", HGRAD)
		array = factory.fluxVars()
		self.assertEqual(array[0].getName(), a.getName())
		self.assertEqual(array[1].getName(), b.getName())
		self.assertEqual(array[2].getName(), c.getName())

	#"""Test VarFactory.py's traceVars() method"""
	def testtraceIDs(self):
		factory = VarFactory()
		a = factory.traceVar("Liam", HGRAD)
		b = factory.traceVar("Crowe", HGRAD)
		c = factory.traceVar("Noris", HGRAD)
		array = factory.traceVars()
		self.assertEqual(array[0].getName(), a.getName())
		self.assertEqual(array[1].getName(), b.getName())
		self.assertEqual(array[2].getName(), c.getName())
# Run the tests:
if (__name__ == '__main__'):
  unittest.main()