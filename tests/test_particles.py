import numpy as np
import pytest
from particles import Particle  # Ersetze 'your_module' mit dem tatsächlichen Modulnamen

def test_particle_initialization():
    """Testet die korrekte Initialisierung eines Partikels."""
    position = [50, 50]
    velocity = [1, -1]
    particle_type = "A"
    color = (255, 0, 0)

    particle = Particle(position, velocity, particle_type, color)

    assert np.all(particle.position == np.array(position))
    assert np.all(particle.velocity == np.array(velocity))
    assert particle.particle_type == particle_type
    assert particle.color == color

def test_particle_move():
    """Testet die Bewegung des Partikels mit toroidalen Randbedingungen und Reibung."""
    particle = Particle([95, 95], [10, 10], "B", (0, 255, 0))
    boundary = (100, 100)
    friction = 0.1

    particle.move(boundary, friction)

    assert 0 <= particle.position[0] < boundary[0], "X-Koordinate sollte sich toroidal anpassen"
    assert 0 <= particle.position[1] < boundary[1], "Y-Koordinate sollte sich toroidal anpassen"
    assert np.all(particle.velocity < [10, 10]), "Reibung sollte die Geschwindigkeit reduzieren"

def test_apply_noise():
    """Testet, ob Rauschen korrekt auf die Geschwindigkeit angewendet wird."""
    particle = Particle([50, 50], [0, 0], "C", (0, 0, 255))
    noise_strength = 0.5

    initial_velocity = particle.velocity.copy()
    particle.apply_noise(noise_strength)

    assert not np.all(initial_velocity == particle.velocity), "Die Geschwindigkeit sollte sich durch das Rauschen ändern"

def test_serialize_deserialize():
    """Testet die Serialisierung und Deserialisierung eines Partikels."""
    particle = Particle([20, 30], [1, -1], "D", (255, 255, 0))
    data = particle.serialize()
    
    new_particle = Particle.deserialize(data)

    assert np.all(new_particle.position == particle.position)
    assert np.all(new_particle.velocity == particle.velocity)
    assert new_particle.particle_type == particle.particle_type
    assert new_particle.color == particle.color
