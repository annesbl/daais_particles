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
        self.position = np.array(position, dtype=float)  #Position as a numpy array
        self.velocity = np.array(velocity, dtype=float)  #Velocity as a numpy array
        self.particle_type = particle_type
        self.color = color if color else (255, 255, 255)  #Default to white if no color is provided
        self.max_influence = max_influence  #Influence range for interaction matrix
        self.size = size

    
    def move(self, boundary, friction):
        """
        Update the particle position and apply friction.
        Implements toroidal boundary conditions (particles wrap around).
        """
        self.position += self.velocity

        #Apply toroidal wrapping (particles reappear on the other side)
        self.position[0] %= boundary[0]  #Wrap X-coordinate
        self.position[1] %= boundary[1]  #Wrap Y-coordinate
        self.velocity *= (1 - friction)  #Apply friction

    
    def apply_noise(self, noise_strength):
        """
        Apply random noise to the particle's velocity.
        """
        self.velocity += np.random.uniform(-noise_strength, noise_strength, size=2)  #Applies random noise to velocity

    
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
