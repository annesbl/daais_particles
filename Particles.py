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
        self.position = np.array(position, dtype=float)  # Using numpy for array operations
        self.velocity = np.array(velocity, dtype=float)  # Using numpy for array operations
        self.particle_type = particle_type
        self.color = color
        self.max_influence = max_influence

    def move(self, boundary, friction):
        """
        Update the particle's position based on its velocity and enforce boundary conditions.
        Apply friction to reduce velocity over time.
        """
        self.position += self.velocity

        # Reflect the particle if it hits the boundary
        if self.position[0] < 0 or self.position[0] > boundary[0]:
            self.velocity[0] = -self.velocity[0]
        if self.position[1] < 0 or self.position[1] > boundary[1]:
            self.velocity[1] = -self.velocity[1]

        # Apply friction
        self.velocity *= (1 - friction)

        # Keep the particle within bounds
        self.position[0] = max(0, min(self.position[0], boundary[0]))
        self.position[1] = max(0, min(self.position[1], boundary[1]))

    def apply_noise(self, noise_strength):
        """
        Apply random noise to the particle's velocity.
        """
        self.velocity += np.random.uniform(-noise_strength, noise_strength, size=2)

    def serialize(self):
        """
        Serialize the particle's data to a dictionary for saving or loading.
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
