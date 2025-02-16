import unittest
from particle_system import ParticleSystem
from matrix import InteractionMatrix

class TestParticleSystem(unittest.TestCase):
    def setUp(self):
        """Set up a test environment for the ParticleSystem."""
        self.types = {"A": (255, 0, 0), "B": (0, 255, 0)}
        self.matrix = InteractionMatrix(list(self.types.keys()))
        self.system = ParticleSystem(10, (100, 100), self.types, self.matrix)

    def test_initialize_particles(self):
        """Test if ParticleSystem initializes the correct number of particles."""
        self.assertEqual(len(self.system.particles), 10)

    def test_update(self):
        """Test if particles update their positions after calling `update()`."""
        initial_positions = [p.position.copy() for p in self.system.particles]

        # Call update (Note: Removed `interaction_strength` because it's not in update())
        self.system.update(noise_strength=0.1, influence_range=50, friction=0.01)

        for i, particle in enumerate(self.system.particles):
            # Ensure that at least one particle moves (with a tolerance for small movements)
            self.assertFalse((particle.position == initial_positions[i]).all(), "Particle position did not change.")

if __name__ == "__main__":
    unittest.main()

