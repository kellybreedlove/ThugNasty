import VarFactory
import unittest

class TestVarFactory(unittest.TestCase):
  """Test VarFactory.py's addNumbers() method"""
  def testTestVar(self):
    VarPtr t = new testVar("Billy Joe", HGRAD, 1) #HGRAD is a random ennum, which I think swig turns into a space
    self.assertEqual(t.getTestID, 1)
    self.assertEqual(t.getName, "Billy Joe")
    self.assertEqual(t.getSpace, HGRAD)
  

# Run the tests:
if (__name__ == '__main__'):
  unittest.main()
