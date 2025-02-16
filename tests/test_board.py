import pytest
import pygame
from board import Board
from unittest.mock import MagicMock


@pytest.fixture
def mock_particle():
    """Fixture to create a mock particle for testing."""
    # Create a mock particle with necessary attributes
    mock_particle = MagicMock()
    mock_particle.position = [100, 100]
    mock_particle.particle_type = "A"
    return mock_particle


@pytest.fixture
def board():
    """Fixture to create a board instance for testing."""
    # Create a board with a 800x600 screen size
    return Board(800, 600)


def test_board_initialization(board):
    """Test that the board initializes properly."""
    assert board.width == 800
    assert board.height == 600
    assert isinstance(board.screen, pygame.Surface)
    assert isinstance(board.clock, pygame.time.Clock)


def test_draw_particles(board, mock_particle):
    """Test that particles are drawn correctly on the board."""
    # Use a mock particle for testing
    particles = [mock_particle]

    # Call the draw_particles method
    board.draw_particles(particles)

    # Check if the particle's position is used in the drawing
    # This will check if pygame.draw.circle is called at least once with the correct arguments
    pygame.draw.circle.assert_called_once_with(board.screen, (255, 0, 0), (100, 100), 3)


def test_get_color_by_type(board):
    """Test that the correct color is returned based on particle type."""
    # Test different particle types
    assert board.get_color_by_type("A") == (255, 0, 0)
    assert board.get_color_by_type("B") == (0, 255, 0)
    assert board.get_color_by_type("C") == (0, 0, 255)
    assert board.get_color_by_type("D") == (255, 255, 0)
    assert board.get_color_by_type("E") == (255, 255, 255)  # Default case


def test_update_display(board, mock_particle):
    """Test that the update_display method works (FPS limiting)."""
    # We can mock clock.tick to test FPS limiting
    board.clock.tick = MagicMock()

    # Call the update_display method
    board.update_display()

    # Check if clock.tick was called once
    board.clock.tick.assert_called_once_with(60)
