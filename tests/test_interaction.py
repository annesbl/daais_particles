import numpy as np
from scipy.spatial import cKDTree
from interaction import KDTree
from interaction import Interactions

def test_initialise_tree():
    particle_array = np.array([[0, 0], [1, 1], [2, 2]])
    tree = KDTree.initialise_tree(particle_array)
    
    assert isinstance(tree, cKDTree)
    assert tree.n == len(particle_array)  # Check if KDTree contains all particles



class MockParticle:
    def __init__(self, position, particle_type):
        self.position = np.array(position)
        self.particle_type = particle_type

class MockInteractionMatrix:
    def get_interaction(self, type_pair):
        return 1.0  # Beispielhafte Wechselwirkungskraft

from unittest.mock import MagicMock

def test_total_force():
    p1 = MockParticle([0, 0], "A")
    p2 = MockParticle([1, 1], "B")
    particles = [p1, p2]
    
    interaction_matrix = MagicMock()  # Mock für die Interaktionsmatrix
    tree = MagicMock()  # Mock für die KDTree

    # Simulation der Wechselwirkungskraft
    interaction_matrix.get_interaction.return_value = 10  # Beispielwert

    # Berechnung der totalen Kraft
    force = np.zeros_like(p1.position, dtype=np.float64)

    assert force.shape == (2,)
    assert not np.all(force == 0)  # Sollte eine Kraft wirken

def test_determine_force():
    p1 = MockParticle([0, 0], "A")
    p2 = MockParticle([1, 1], "B")
    
    interaction_matrix = MockInteractionMatrix()
    
    distance_vector = p2.position - p1.position
    distance = np.linalg.norm(distance_vector)
    
    force = Interactions.determine_force(p1, p2, interaction_matrix, distance_vector, distance)
    
    assert force.shape == (2,)
    assert not np.all(force == 0)  # Sollte eine Kraft wirken
