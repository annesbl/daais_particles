import unittest
from unittest.mock import patch, MagicMock
from simulation import Simulation
from particle_system import ParticleSystem
from board import Board
from matrix import InteractionMatrix

class TestSimulation(unittest.TestCase):

    @patch("pygame.display.set_mode")
    def test_initialization(self, mock_set_mode):
        # Mock the interaction matrix
        interaction_matrix = MagicMock(spec=InteractionMatrix)
        
        # Initialize the simulation
        simulation = Simulation(800, 600, 1000, ["A", "B", "C", "D"], interaction_matrix)

        # Check if the simulation was initialized correctly
        self.assertEqual(simulation.width, 800)
        self.assertEqual(simulation.height, 600)
        self.assertEqual(simulation.particle_system.particle_count, 1000)
        self.assertEqual(len(simulation.particle_system.particles), 1000)
        self.assertTrue(simulation.running)

    @patch("pygame.event.get", return_value=[MagicMock(type=pygame.QUIT)])
    def test_handle_events_quit(self, mock_events):
        # Mock the interaction matrix
        interaction_matrix = MagicMock(spec=InteractionMatrix)
        
        # Initialize the simulation
        simulation = Simulation(800, 600, 1000, ["A", "B", "C", "D"], interaction_matrix)
        
        # Call handle_events() method
        simulation.handle_events()

        # Check if the running flag was set to False after quitting
        self.assertFalse(simulation.running)

    @patch("pygame.event.get", return_value=[])
    @patch.object(ParticleSystem, "update")
    @patch.object(Board, "draw_particles")
    @patch.object(Board, "update_display")
    def test_run_update_render(self, mock_update_display, mock_draw_particles, mock_update, mock_events):
        # Mock the interaction matrix
        interaction_matrix = MagicMock(spec=InteractionMatrix)
        
        # Initialize the simulation
        simulation = Simulation(800, 600, 1000, ["A", "B", "C", "D"], interaction_matrix)
        
        # Mock that the simulation is running for just one loop
        simulation.running = True

        # Run one iteration of the simulation loop
        simulation.update()
        simulation.render()

        # Verify that the update and render methods were called
        mock_update.assert_called_once()
        mock_draw_particles.assert_called_once()
        mock_update_display.assert_called_once()

    @patch("pygame.event.get", return_value=[MagicMock(type=pygame.QUIT)])
    def test_run_quit(self, mock_events):
        # Mock the interaction matrix
        interaction_matrix = MagicMock(spec=InteractionMatrix)
        
        # Initialize the simulation
        simulation = Simulation(800, 600, 1000, ["A", "B", "C", "D"], interaction_matrix)

        # Run the simulation loop and quit after one cycle
        simulation.run()

        # Check if the simulation has stopped running
        self.assertFalse(simulation.running)

if __name__ == "__main__":
    unittest.main()
