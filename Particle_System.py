import random 
import pygame 
from Particles import Particle

class ParticleSystem:
    def __init__(self, particle_count, boundary, types, interaction_matrix):
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
        particles = []
        for _ in range(count):
            position = [random.uniform(0, boundary[0]), random.uniform(0, boundary[1])]
            velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
            particle_type = random.choice(list(types.keys()))
            color = types[particle_type]
            particles.append(Particle(position, velocity, particle_type, color))
        return particles

    def apply_interactions(self, interaction_strength, influence_range):
        """
        Apply interactions between particles based on their types and distances.
        """
        for i, particle in enumerate(self.particles):
            for j, other in enumerate(self.particles):
                if i == j:
                    continue

                # Calculate the distance
                dx = other.position[0] - particle.position[0]
                dy = other.position[1] - particle.position[1]
                distance = (dx**2 + dy**2)**0.5

                # Skip if particles are outside the influence range
                if distance > influence_range:
                    continue

                # Get the interaction value from the matrix
                interaction = self.interaction_matrix[particle.particle_type][other.particle_type]

                # Apply forces based on interaction
                force = interaction_strength * interaction / (distance + 1e-6)
                particle.velocity[0] += force * (dx / distance)
                particle.velocity[1] += force * (dy / distance)

    def update(self, noise_strength=0.1, interaction_strength=0.1, influence_range=50, friction=0.01):
        """
        Update all particles for one simulation step.
        - Apply interactions.
        - Apply random noise.
        - Move particles based on their velocities.
        """
        self.apply_interactions(interaction_strength, influence_range)
        for particle in self.particles:
            particle.apply_noise(noise_strength)
            particle.move(self.boundary, friction)

    def visualize(self, screen):
        """
        Visualize all particles on the screen.
        """
        screen.fill((0, 0, 0))  # Clear screen
        for particle in self.particles:
            pygame.draw.circle(screen, particle.color, (int(particle.position[0]), int(particle.position[1])), 5)
        pygame.display.flip()

    def serialize_particles(self):
        """
        Serialize all particles in the system for saving.
        """
        return [particle.serialize() for particle in self.particles]

    def deserialize_particles(self, serialized_particles):
        """
        Deserialize particle data and recreate the particle system.
        """
        self.particles = [Particle.deserialize(data) for data in serialized_particles]

    def save_to_file(self, filename):
        """
        Save all serialized particle data to a JSON file.
        """
        import json
        with open(filename, 'w') as f:
            json.dump(self.serialize_particles(), f)

    def load_from_file(self, filename):
        """
        Load particle data from a JSON file and recreate the particle system.
        """
        import json
        with open(filename, 'r') as f:
            serialized_particles = json.load(f)
        self.deserialize_particles(serialized_particles)

