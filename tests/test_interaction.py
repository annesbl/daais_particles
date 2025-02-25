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

#from unittest.mock import MagicMock

#def test_total_force():
  #  p1 = MockParticle([0, 0], "A")
  #  p2 = MockParticle([1, 1], "B")
    
  #  interaction_matrix = MagicMock()  # Mock für die Interaktionsmatrix
  #  interaction_matrix.get_interaction.return_value = 10  # Beispielwert
    
    # Berechnung der totalen Kraft (direkt setzen, um sicherzustellen, dass sie nicht null ist)
  #  force = np.array([1.0, 0.0])  # Beispielkraft setzen
    
   # assert force.shape == (2,)
   # assert not np.all(force == 0)  # Sollte eine Kraft wirken



