import pytest
import numpy as np
from particles import Particle
from interaction import KDTree, Implementation
from matrix import InteractionMatrix  # Falls die Klasse hier gespeichert ist
from particle_system import ParticleSystem  # Ersetze mit deinem Modulnamen


@pytest.fixture
def sample_particle_system():
    """Erzeugt ein Beispiel-ParticleSystem für die Tests."""
    particle_count = 10
    boundary = (100, 100)
    types = {"A": (255, 0, 0), "B": (0, 255, 0), "C": (0, 0, 255), "D": (255, 255, 0)}
    interaction_matrix = InteractionMatrix(types.keys())

    return ParticleSystem(particle_count, boundary, types, interaction_matrix)


def test_initialize_particles(sample_particle_system):
    """Testet, ob die Partikel korrekt initialisiert werden."""
    ps = sample_particle_system

    assert len(ps.particles) == 10  # Überprüft, ob alle Partikel erstellt wurden
    for particle in ps.particles:
        assert 0 <= particle.position[0] <= ps.boundary[0]
        assert 0 <= particle.position[1] <= ps.boundary[1]
        assert -1 <= particle.velocity[0] <= 1
        assert -1 <= particle.velocity[1] <= 1
        assert particle.particle_type in ps.types


def test_update_particles(sample_particle_system):
    """Testet, ob das Update die Partikelpositionen verändert."""
    ps = sample_particle_system
    initial_positions = np.array([p.position.copy() for p in ps.particles])

    ps.update(noise_strength=0.05, influence_range=50, friction=0.01)

    updated_positions = np.array([p.position for p in ps.particles])
    assert not np.array_equal(initial_positions, updated_positions)  # Positionen müssen sich ändern


def test_update_noise_effect(sample_particle_system):
    """Testet, ob Rauschstärke die Bewegung beeinflusst."""
    ps = sample_particle_system
    initial_positions = np.array([p.position.copy() for p in ps.particles])

    ps.update(noise_strength=1.0, influence_range=50, friction=0.01)

    updated_positions = np.array([p.position for p in ps.particles])
    assert not np.array_equal(initial_positions, updated_positions)  # Änderungen durch Rauschen erwartet


def test_particle_colors(sample_particle_system):
    """Testet, ob Partikel die richtigen Farben zugeordnet bekommen."""
    ps = sample_particle_system

    for particle in ps.particles:
        assert particle.color == ps.types[particle.particle_type]  # Farbe muss mit Typ übereinstimmen


def test_kdtree_initialization(sample_particle_system):
    """Testet, ob KDTree korrekt erstellt wird."""
    ps = sample_particle_system
    positions = [p.position for p in ps.particles]

    tree = KDTree.initialise_tree(positions)
    assert tree is not None
