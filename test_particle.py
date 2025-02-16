import unittest
import numpy as np
from particles import Particle

class TestParticle(unittest.TestCase):

    def setUp(self):
        self.particle = Particle(position=[50, 50], velocity=[5, 5], particle_type="A", color=(255, 0, 0))

    def test_move_within_boundary(self):
        self.particle.move(boundary=(100, 100), friction=0.1)
        self.assertTrue(np.allclose(self.particle.position, [55, 55]))
        self.assertTrue(np.allclose(self.particle.velocity, [4.5, 4.5]))

    def test_apply_noise(self):
        initial_velocity = self.particle.velocity.copy()
        self.particle.apply_noise(0.5)
        self.assertFalse(np.allclose(self.particle.velocity, initial_velocity))

    def test_serialize_and_deserialize(self):
        serialized_data = self.particle.serialize()
        new_particle = Particle.deserialize(serialized_data)
        self.assertEqual(new_particle.particle_type, self.particle.particle_type)
        self.assertTrue(np.allclose(new_particle.position, self.particle.position))

if __name__ == "__main__":
    unittest.main()
