import pytest
import numpy as np
from particle_system import ParticleSystem
from matrix import InteractionMatrix

@pytest.fixture
def particle_system():
    return ParticleSystem(10, (100, 100), {"A": None, "B": None}, InteractionMatrix(["A", "B"]))

def test_particle_system_initialization(particle_system):
    assert len(particle_system.particles) == 10

def test_particle_system_update(particle_system):
    try:
        particle_system.update()
    except Exception as e:
        pytest.fail(f"update failed: {e}")
