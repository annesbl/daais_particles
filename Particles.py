import random
import numpy as np

class Particle:
    def __init__(self, position, velocity, particle_type, color=None, max_influence=100, size=5):
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
        self.size = size

    def move(self, boundary, friction):
        # Update position
        self.position += self.velocity

        # Apply toroidal wrapping
        self.position[0] %= boundary[0]  # Wrap X-coordinate
        self.position[1] %= boundary[1]  # Wrap Y-coordinate

        # Apply friction
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

    def draw_particles_with_trails(self, particles):
        self.trail_surface.fill((0, 0, 0, 10))  # Use semi-transparent surface
        for particle in particles:
            x, y = int(particle.position[0]) % self.width, int(particle.position[1]) % self.height
            pygame.draw.circle(self.trail_surface, particle.color, (x, y), particle.size)
        self.screen.blit(self.trail_surface, (0, 0))

