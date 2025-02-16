import pytest
import numpy as np
from interaction import Interactions
from particle import Particle
from matrix import InteractionMatrix

@pytest.fixture
def interaction_matrix():
    return InteractionMatrix(["A", "B", "C"], {("A", "B"): 0.5, ("A", "C"): -0.2})

@pytest.fixture
def particles():
    return [
        Particle([0, 0], [0, 0], "A"),
        Particle([1, 1], [0, 0], "B"),
    ]

def test_total_force(particles, interaction_matrix):
    force = Interactions.total_force(particles[0], particles[1], interaction_matrix)
    assert len(force) == 2
