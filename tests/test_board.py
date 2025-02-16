import pytest
import pygame
from board import Board

class MockParticle:
    def __init__(self, position, particle_type):
        self.position = position
        self.particle_type = particle_type

@pytest.fixture
def board():
    return Board(800, 600)

@pytest.fixture
def particles():
    return [
        MockParticle((100, 100), "A"),
        MockParticle((200, 200), "B"),
        MockParticle((300, 300), "C"),
        MockParticle((400, 400), "D"),
    ]

def test_board_initialization(board):
    assert board.width == 800
    assert board.height == 600
    assert isinstance(board.screen, pygame.Surface)
    assert isinstance(board.clock, pygame.time.Clock)

def test_get_color_by_type(board):
    assert board.get_color_by_type("A") == (255, 0, 0)
    assert board.get_color_by_type("B") == (0, 255, 0)
    assert board.get_color_by_type("C") == (0, 0, 255)
    assert board.get_color_by_type("D") == (255, 255, 0)
    assert board.get_color_by_type("X") == (255, 255, 255)  # Default color

def test_draw_particles(board, particles):
    board.draw_particles(particles)
    assert board.screen is not None  # Ensure screen is still valid after drawing

def test_update_display(board):
    board.update_display()
    assert board.clock.get_fps() >= 0  # FPS should be measurable


