import unittest
import numpy as np
from InteractionMatrix import InteractionMatrix
from Particle import Particle


class TestInteractionMatrix(unittest.TestCase):

    def setUp(self):
        self.types = ["A", "B", "C"]
        self.matrix = InteractionMatrix(self.types)

    def test_matrix_initialization(self):
        self.assertEqual(self.matrix.matrix.shape, (3, 3))