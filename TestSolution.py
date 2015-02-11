import Solution
import PoissonFormulation
import StokesVGPFormulation
from Var import *
import MeshFactory
import Mesh
import Function
import BC
import RHS
import IP
import unittest

class TestSolution(unittest.TestCase):

    """Test Solution.py's Solution() constructor"""
    def test_Solution(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        self.assertNotEqual(s, None) #make sure some object exists


    #"""Test Solution.py's Solution() copy constructor"""
    #def test_Solution(self):
        #poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        #poissonBF = poissonForm.bf()
        #mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        #s1 = Solution.Solution_solution(mesh2)
        #s2 = Solution.Solution(s1)
        #self.assertEqual(s1, s2) #make sure some object exists


    """Test Solution.py's addSolution() method"""
    def test_addSolution(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        t = Solution.Solution_solution(mesh2)
        s.addSolution(s,1.0)
        self.assertNotEqual(s,t) #s != t since s had something added to it since it was copied
  
        # again with different params for addSolution
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)

        x = Function.Function_xn(1)
        one = Function.Function_constant(1)
        zero = Function.Function_constant(0)

        s = Solution.Solution_solution(mesh2)
        t = Solution.Solution_solution(mesh2)
        s.projectOntoMesh({
                phi.ID() : x,
                psi.ID() : Function.Function_vectorize(one,zero)
          })
        s.addSolution(s,1.0,[phi.ID()])
        self.assertNotEqual(s,t) #s != t since s had something added to it since it was copied


    """Test Solution.py's clear() method"""
    def test_clear(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        s.clear()
        self.assertNotEqual(s, None) #make sure some object exists


    """Test Solution.py's setCubatureEnrichmentDegree() & cubatureEnrichmentDegree() method"""
    def test_cubatureEnrichmentDegree(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh2)
        s.setCubatureEnrichmentDegree(3)
        self.assertEqual(3, s.cubatureEnrichmentDegree())
        s.setCubatureEnrichmentDegree(4)
        self.assertEqual(4, s.cubatureEnrichmentDegree())
        self.assertNotEqual(3, s.cubatureEnrichmentDegree())


    """Test Solution.py's L2NormOfSolution() method"""
    def test_L2NormOfSolution(self):
         poissonForm = PoissonFormulation.PoissonFormulation(2, True)
         poissonBF = poissonForm.bf()
         mesh2 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
         s = Solution.Solution_solution(mesh2)
         self.assertEqual(0.0, s.L2NormOfSolution(0))

         x = Function.Function_xn(1)
         one = Function.Function_constant(1)
         zero = Function.Function_constant(0)
         phi = poissonForm.phi() # VarPtr for main, scalar-valued variable in Poisson problem
         psi = poissonForm.psi() # VarPtr for gradient of psi, vector-valued
         r = Solution.Solution_solution(mesh2)
         r.projectOntoMesh({ phi.ID() : x, psi.ID() : Function.Function_vectorize(one,zero)})
         r.addSolution(r,1.0,[phi.ID()])
         self.assertAlmostEqual(1.34, r.L2NormOfSolution(0))
         self.assertAlmostEqual(216, r.L2NormOfSolution(1))

    
    #"""Test Solution.py's projectOntoMesh() method"""
    #def test_projectOntoMesh(self):

    #"""Test Solution.py's energyErrorTotal() method"""
    #def test_energyErrorTotal(self):

    #"""Test Solution.py's setWriteMatrixToFile() method"""
    #def test_setWriteMatrixToFile(self):

    #"""Test Solution.py's setWriteMatrixToMatrixMarketFile() method"""
    #def test_setWriteMatrixToMatrixMarketFile(self):
        
 #"""Test Solution.py's setWriteRHSToMatrixMarketFile() method"""
    #def test_setWriteMatrixToMatrixMarketFile(self):
        
    """Test Solution.py's mesh() method"""
    def test_mesh(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh1 = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh1)
        self.assertEqual(mesh1, s.mesh())
       

    """Test Solution.py's setBC() and bc() method"""
    def test_bc(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        bc = BC.BC_bc()
        s.setBC(bc)
        self.assertEqual(bc, s.bc())


    """Test Solution.py's setRHS() and rhs() method"""
    def test_rhs(self):
        poissonForm = PoissonFormulation.PoissonFormulation(2, True)
        poissonBF = poissonForm.bf()
        mesh = MeshFactory.MeshFactory_rectilinearMesh(poissonBF,[1.0,1.0],[2,3],4)
        s = Solution.Solution_solution(mesh)
        rhs = RHS.RHS_rhs()
        s.setRHS(rhs)
        self.assertEqual(rhs, s.rhs())


    #"""Test Solution.py's setIP() and ip() method"""
    #def test_ip(self):


        

    #"""Test Solution.py's save() method"""
    #def test_save(self):

    #"""Test Solution.py's load() method"""
    #def test_load(self):

    #"""Test Solution.py's saveToHDF5() method"""
    #def test_saveToHDF5(self):

    #"""Test Solution.py's loadFromHDF5() method"""
    #def test_loadFromHDF5(self):

    #"""Test Solution.py's setUseCondensedSolve() method"""
    #def test_setUseCondensedSolve(self):




    # Run the tests:
    if (__name__ == '__main__'):
        unittest.main()
