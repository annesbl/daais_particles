import random 

class Particle:
    def __init__(self, position, velocity, particle_type, color):
        """
        Initialize a single particle.

        Parameters:
        - position (list): [x, y] coordinates of the particle.
        - velocity (list): [vx, vy] velocity of the particle.
        - particle_type (str): Type of the particle. (4 typen)
        - color (tuple): RGB color representing the particle type.
        """
        self.position = position
        self.velocity = velocity
        self.particle_type = particle_type
        self.color = color
        
    def move(self, boundary, friction):
        """
        Update the particle's position based on its velocity and enforce boundary conditions.
        Apply friction to reduce velocity over time.
        """
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Reflect the particle if it hits the boundary
        # code hier

        # Apply friction
        # code hier 
    
        # Keep the particle within bounds
        # code hier 

    def apply_noise(self, noise_strength):
        """
        Apply random noise to the particle's velocity.
        """
        pass


    def serialize(self):
        """
        Serialize the particle's data to a dictionary for saving or loading.
        """
        return {
            "position": self.position,
            "velocity": self.velocity,
            "particle_type": self.particle_type,
            "color": self.color
        }

    @classmethod
    def deserialize(cls, data):
        """
        Create a particle instance from serialized data.
        """
        return cls(data["position"], data["velocity"], data["particle_type"], data["color"])
 

class ParticleSystem:
    def __init__(self, particle_count, boundary, types):
        """
        Initialize a particle system with multiple particles.

        Parameters:
        - particle_count (int): Number of particles to initialize.
        - boundary (tuple): Size of the simulation area (width, height).
        - types (dict): Dictionary of particle types and their colors.
        - interaction_matrix (dict): Matrix defining interactions between particle types.
        """
        self.particles = self.initialize_particles(particle_count, boundary, types)
        self.boundary = boundary
        self.types = types
        self.interaction_matrix = interaction_matrix

    def initialize_particles(self, count, boundary, types):
        """
        Initialize multiple particles with random attributes.

        Returns:
        - list: A list of Particle instances.
        """
        pass

    def apply_interactions(self, interaction_strength, influence_range):
        """
        Apply interactions between particles based on their types and distances.
        """
        pass
    
        # Calculate the distance
        # code hier 
            
        # Skip if particles are outside the influence range
        # code hier 

        # Get the interaction value from the matrix
        # code hier
            
        # Apply forces based on interaction
        # code hier 

    def update(self, noise_strength, interaction_strength, influence_range, friction):
        """
        Update all particles for one simulation step.
        - Apply interactions.
        - Apply random noise.
        - Move particles based on their velocities.
        """
        pass

    def visualize(self, screen):
        """
        Visualize all particles on the screen.
        """
        pass

    def serialize_particles(self):
        """
        Serialize all particles in the system for saving.
        """
        pass

    def deserialize_particles(self, serialized_particles):
        """
        Deserialize particle data and recreate the particle system.
        """
        pass 
