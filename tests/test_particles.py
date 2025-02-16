import pytest
import numpy as np
from particles import Particle


@pytest.fixture
def sample_particle():
    """Erzeugt eine Beispiel-Partikelinstanz für Tests."""
    position = [50, 50]
    velocity = [1, -1]
    particle_type = "A"
    color = (255, 0, 0)  # Rot
    return Particle(position, velocity, particle_type, color)


def test_particle_initialization(sample_particle):
    """Testet, ob ein Partikel korrekt initialisiert wird."""
    p = sample_particle
    assert np.array_equal(p.position, np.array([50, 50]))
    assert np.array_equal(p.velocity, np.array([1, -1]))
    assert p.particle_type == "A"
    assert p.color == (255, 0, 0)
    assert p.max_influence == 100
    assert p.size == 5


def test_particle_movement(sample_particle):
    """Testet, ob das Partikel sich korrekt bewegt."""
    p = sample_particle
    boundary = (100, 100)
    friction = 0.1

    p.move(boundary, friction)

    assert np.allclose(p.position, np.array([51, 49]))  # Position sollte sich ändern
    assert np.allclose(p.velocity, np.array([0.9, -0.9]))  # Friction sollte angewendet werden


def test_toroidal_wrapping():
    """Testet, ob das Partikel sich toroidal um den Rand bewegt."""
    p = Particle(position=[99, 99], velocity=[2, 2], particle_type="B")
    boundary = (100, 100)
    friction = 0.0  # Keine Reibung für einfachen Test

    p.move(boundary, friction)

    assert np.allclose(p.position, np.array([1, 1]))  # Sollte sich um den Rand wickeln


def test_apply_noise(sample_particle):
    """Testet, ob zufälliges Rauschen zur Geschwindigkeit hinzugefügt wird."""
    p = sample_particle
    initial_velocity = p.velocity.copy()
    noise_strength = 0.5

    p.apply_noise(noise_strength)

    assert not np.array_equal(p.velocity, initial_velocity)  # Velocity sollte sich durch Rauschen ändern
    assert np.all(np.abs(p.velocity - initial_velocity) <= noise_strength)  # Änderung darf nicht zu groß sein


def test_serialization(sample_particle):
    """Testet, ob die Serialisierung und Deserialisierung korrekt funktionieren."""
    p = sample_particle
    serialized = p.serialize()
    deserialized = Particle.deserialize(serialized)

    assert np.array_equal(p.position, deserialized.position)
    assert np.array_equal(p.velocity, deserialized.velocity)
    assert p.particle_type == deserialized.particle_type
    assert p.color == deserialized.color
