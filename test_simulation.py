import unittest
from Simulation import Simulation

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.simulation = Simulation(800, 600, 100, ["A", "B", "C"])

    def test_initialization(self):
        self.assertEqual(self.simulation.width, 800)
        self.assertEqual(self.simulation.height, 600)
        self.assertEqual(len(self.simulation.particle_system.particles), 100)

    def test_update(self):
        initial_positions = [p.position.copy() for p in self.simulation.particle_system.particles]
        self.simulation.update()
        for i, particle in enumerate(self.simulation.particle_system.particles):
            self.assertFalse((particle.position == initial_positions[i]).all())

if __name__ == "__main__":
    unittest.main()