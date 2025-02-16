import pytest
import numpy as np
from interaction import Implementation, KDTree
from particles import Particle
from matrix import InteractionMatrix

@pytest.fixture
def particles():
    return [
        Particle([0, 0], [0, 0], "A"),
        Particle([1, 1], [0, 0], "B"),
    ]

@pytest.fixture
def interaction_matrix():
    return InteractionMatrix(["A", "B"], {("A", "B"): 0.5})

def test_update_particles(particles, interaction_matrix):
    positions = np.array([p.position for p in particles])
    tree = KDTree.initialise_tree(positions)
    
    impl = Implementation()
    updated_particles = impl.update_particles(tree, 10, particles, interaction_matrix, (100, 100), 0.1)
    
    assert len(updated_particles) == len(particles)
