import pytest
import pygame
from simulation import Simulation
from matrix import InteractionMatrix

@pytest.fixture
def simulation():
    interaction_matrix = InteractionMatrix(["A", "B"])
    return Simulation(800, 600, 10, ["A", "B"], interaction_matrix)

def test_simulation_initialization(simulation):
    assert simulation.width == 800
    assert simulation.height == 600

def test_simulation_update(simulation):
    try:
        simulation.update()
    except Exception as e:
        pytest.fail(f"Simulation update failed: {e}")
