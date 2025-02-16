import unittest
from Particle_System import ParticleSystem
from matrix import InteractionMatrix

class TestParticleSystem(unittest.TestCase):
    def setUp(self):
        self.types = {"A": (255, 0, 0), "B": (0, 255, 0)}
        self.matrix = InteractionMatrix(list(self.types.keys()))
        self.system = ParticleSystem(10, (100, 100), self.types, self.matrix)

    def test_initialize_particles(self):
        self.assertEqual(len(self.system.particles), 10)

    def test_apply_interactions(self):
        initial_velocity = self.system.particles[0].velocity.copy()
        self.system.apply_interactions(interaction_strength=0.1, influence_range=50)
        self.assertFalse((self.system.particles[0].velocity == initial_velocity).all())
    def test_update(self):
        initial_positions = [p.position.copy() for p in self.system.particles]
        self.system.update(noise_strength=0.1, interaction_strength=0.1, influence_range=50, friction=0.01)
        for i, particle in enumerate(self.system.particles):
            self.assertFalse((particle.position == initial_positions[i]).all())

if __name__ == "__main__":
    unittest.main()
