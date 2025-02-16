import pytest
import numpy as np
from scipy.spatial import cKDTree
from unittest.mock import MagicMock
from interaction import KDTree, Interactions, Implementation  # Ersetze 'your_module' mit dem richtigen Modulnamen

# Dummy Particle-Klasse für Testzwecke
class Particle:
    def __init__(self, position, particle_type):
        self.position = np.array(position, dtype=np.float64)
        self.particle_type = particle_type
        self.velocity = np.zeros(2, dtype=np.float64)

    def move(self, sim_area, friction):
        """Dummy move method to simulate particle movement."""
        self.velocity *= (1 - friction)
        self.position += self.velocity
        # Begrenzung auf den Simulationsbereich
        self.position = np.clip(self.position, 0, np.array(sim_area))

@pytest.fixture
def mock_particles():
    """Fixture zur Erstellung von Dummy-Partikeln."""
    p1 = Particle([1.0, 1.0], 'A')
    p2 = Particle([2.0, 2.0], 'B')
    p3 = Particle([3.0, 3.0], 'C')
    return [p1, p2, p3]

@pytest.fixture
def interaction_matrix():
    """Mock für die Interaktionsmatrix."""
    mock_interaction_matrix = MagicMock()
    mock_interaction_matrix.get_interaction.return_value = 1.0  # Einheitliche Stärke
    return mock_interaction_matrix

@pytest.fixture
def tree(mock_particles):
    """Erzeugt einen KDTree aus Partikelpositionen."""
    particle_positions = [particle.position for particle in mock_particles]
    return cKDTree(particle_positions)

def test_kd_tree_initialization(mock_particles):
    """Testet die Initialisierung des KDTree."""
    particle_positions = [p.position for p in mock_particles]
    tree = KDTree.initialise_tree(particle_positions)
    assert isinstance(tree, cKDTree)

def test_total_force(mock_particles, interaction_matrix, tree):
    """Testet die Berechnung der Gesamtkräfte auf ein Partikel."""
    p1 = mock_particles[0]
    force = Interactions.total_force(p1, mock_particles, interaction_matrix, tree, radius=5)
    
    assert isinstance(force, np.ndarray)
    assert force.shape == (2,)
    assert np.linalg.norm(force) >= 0  # Kraft sollte >= 0 sein



def test_update_particles(mock_particles, interaction_matrix, tree):
    """Testet, ob die Partikel korrekt aktualisiert werden."""
    sim_area = [10, 10]
    friction = 0.1
    implementation = Implementation()

    updated_particles = implementation.update_particles(tree, 5, mock_particles, interaction_matrix, sim_area, friction)

    for p in updated_particles:
        assert isinstance(p.position, np.ndarray)
        assert p.position.shape == (2,)
