import numpy as np
import pytest
from particle_system import ParticleSystem  
from particles import Particle
from matrix import InteractionMatrix


class MockParticle(Particle):
    """Mock-Klasse für Partikel mit einer fixierten `apply_noise`-Methode."""
    def apply_noise(self, noise_strength):
        self.velocity += np.random.uniform(-noise_strength, noise_strength, size=2)

@pytest.fixture
def mock_particle_system():
    """Fixture zur Erstellung eines Partikelsystems mit Mock-Daten."""
    particle_count = 10
    boundary = (100, 100)
    types = {"A": (255, 0, 0), "B": (0, 255, 0)}
    interaction_matrix = InteractionMatrix(types.keys())

    system = ParticleSystem(particle_count, boundary, types, interaction_matrix)
    system.particles = [MockParticle(p.position, p.velocity, p.particle_type, p.color) for p in system.particles]
    return system

def test_initialize_particles(mock_particle_system):
    """Testet, ob Partikel korrekt initialisiert werden."""
    system = mock_particle_system
    assert len(system.particles) == 10
    for particle in system.particles:
        assert 0 <= particle.position[0] <= 100
        assert 0 <= particle.position[1] <= 100
        assert particle.particle_type in ["A", "B"]

from unittest.mock import MagicMock



