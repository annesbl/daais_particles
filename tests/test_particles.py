import pytest
import numpy as np
from particles import Particle

def test_particle_initialization():
    p = Particle([10, 10], [1, 1], "A")
    assert np.allclose(p.position, [10, 10])
    assert np.allclose(p.velocity, [1, 1])
    assert p.particle_type == "A"
    assert p.color == (255, 255, 255)

def test_particle_move():
    p = Particle([10, 10], [1, 1], "A")
    p.move([100, 100], 0.1)
    assert np.allclose(p.position, [11, 11])

def test_particle_apply_noise():
    p = Particle([10, 10], [1, 1], "A")
    p.apply_noise(0.5)
    assert len(p.velocity) == 2
