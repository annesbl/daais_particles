import pytest
import pygame
import numpy as np
from unittest.mock import MagicMock, patch
from simulation import Simulation
from matrix import InteractionMatrix


@pytest.fixture
def simulation():
    """Erzeugt eine Simulation-Instanz für Tests mit Mocking von Pygame."""
    width, height = 800, 600
    particle_count = 100
    particle_types = ["A", "B", "C", "D"]
    
    custom_interactions = {
        ("A", "B"): 20.0,
        ("A", "C"): -44.0,
        ("B", "C"): 8.0,
        ("D", "A"): -33.0,
        ("A", "A"): -100.0,
        ("B", "B"): 100.0,
        ("C", "C"): 29.0,
        ("D", "D"): -18.0,
    }
    interaction_matrix = InteractionMatrix(particle_types, custom_interactions)

    sim = Simulation(width, height, particle_count, particle_types, interaction_matrix)
    
    # Mocking Pygame-Funktionen, um Tests ohne UI durchzuführen
    sim.board = MagicMock()
    return sim


def test_simulation_initialization(simulation):
    """Testet, ob die Simulation korrekt initialisiert wird."""
    assert simulation.width == 800
    assert simulation.height == 600
    assert simulation.running is True
    assert len(simulation.particle_system.particles) == 100
    assert isinstance(simulation.interaction_matrix, InteractionMatrix)


@patch("pygame.event.get", return_value=[pygame.event.Event(pygame.QUIT)])
def test_handle_events_quit(mock_pygame_event, simulation):
    """Testet, ob die Simulation bei einem QUIT-Event korrekt beendet wird."""
    simulation.handle_events()
    assert simulation.running is False


def test_update_calls_particle_system_update(simulation):
    """Testet, ob `update` die `update`-Methode des Partikelsystems aufruft."""
    simulation.particle_system.update = MagicMock()
    simulation.update()
    simulation.particle_system.update.assert_called_once()


def test_render_calls_board_functions(simulation):
    """Testet, ob `render` die Zeichenfunktionen des Boards aufruft."""
    simulation.render()
    simulation.board.draw_particles.assert_called_once()
    simulation.board.update_display.assert_called_once()
