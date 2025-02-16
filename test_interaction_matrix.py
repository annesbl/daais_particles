import unittest
import numpy as np
from matrix import InteractionMatrix
from particles import Particle


class TestInteractionMatrix(unittest.TestCase):

    def setUp(self):
        self.types = ["A", "B", "C"]
        self.matrix = InteractionMatrix(self.types)

    def test_matrix_initialization(self):
        self.assertEqual(self.matrix.matrix.shape, (3, 3))
        
    def test_get_interaction(self):
        interaction = self.matrix.get_interaction("A", "B")
        self.assertTrue(-1 <= interaction <= 1)

    def test_calculate_force(self):
        particle1 = Particle(position=[0, 0], velocity=[0, 0], particle_type="A")
        particle2 = Particle(position=[3, 4], velocity=[0, 0], particle_type="B")
        force = self.matrix.calculate_force(particle1, particle2)
        self.assertEqual(force.shape, (2,))
        
if __name__ == "__main__":
    unittest.main()