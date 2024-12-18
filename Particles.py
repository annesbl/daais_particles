import random
import numpy as np

class Particle:
    def __init__(self, position, velocity, particle_type, color=None, max_influence=100):
        """
        Initialize a single particle.

        Parameters:
        - position (list): [x, y] coordinates of the particle.
        - velocity (list): [vx, vy] velocity of the particle.
        - particle_type (str): Type of the particle.
        - color (tuple): RGB color representing the particle type.
        - max_influence (int): Maximum influence range of the particle.
        """
        self.position = np.array(position, dtype=float)  # Position as a numpy array
        self.velocity = np.array(velocity, dtype=float)  # Velocity as a numpy array
        self.particle_type = particle_type
        self.color = color  # RGB color
        self.max_influence = max_influence  # Influence range for interaction matrix

    def move(self, boundary, friction):
        """
        Update particle position based on velocity, enforce boundaries, and apply friction.
        """
        self.position += self.velocity

        # Boundary reflections
        for i in range(2):  # 0: x-axis, 1: y-axis
            if self.position[i] < 0 or self.position[i] > boundary[i]:
                self.velocity[i] = -self.velocity[i]
                self.position[i] = max(0, min(self.position[i], boundary[i]))

        # Apply friction to reduce velocity
        self.velocity *= (1 - friction)

    def apply_noise(self, noise_strength):
        """
        Apply random noise to the particle's velocity.
        """
        self.velocity += np.random.uniform(-noise_strength, noise_strength, size=2)

    def serialize(self):
        """
        Serialize the particle's data to a dictionary.
        """
        return {
            "position": self.position.tolist(),
            "velocity": self.velocity.tolist(),
            "particle_type": self.particle_type,
            "color": self.color,
        }

    @classmethod
    def deserialize(cls, data):
        """
        Create a particle instance from serialized data.
        """
        return cls(data["position"], data["velocity"], data["particle_type"], data["color"])
