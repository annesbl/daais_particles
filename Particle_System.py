import random
import pygame
import numpy as np
from Particles import Particle

class ParticleSystem:
    def __init__(self, particle_count, boundary, types, interaction_matrix):
        """
        Initialize a particle system with multiple particles.

        Parameters:
        - particle_count (int): Number of particles.
        - boundary (tuple): Size of the simulation area (width, height).
        - types (dict): Dictionary of particle types and their colors.
        - interaction_matrix (InteractionMatrix): Interaction matrix instance.
        """
        self.particles = self.initialize_particles(particle_count, boundary, types)
        self.boundary = boundary
        self.types = types
        self.interaction_matrix = interaction_matrix

    def initialize_particles(self, count, boundary, types):
        """
        Create particles with random positions, velocities, and types.
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
        Apply optimized interactions between particles using early distance filtering.
        """
        particle_count = len(self.particles)
        for i in range(particle_count):
            particle = self.particles[i]
            total_force = np.array([0.0, 0.0])
            for j in range(i + 1, particle_count):  # Avoid duplicate calculations
                other = self.particles[j]

                # Calculate distance vector and magnitude
                distance_vector = other.position - particle.position
                distance = np.linalg.norm(distance_vector)

                # Skip if particles are too far apart
                if distance == 0 or distance > influence_range:
                    continue

                # Calculate force using interaction strength
                interaction = self.interaction_matrix.get_interaction(particle.particle_type, other.particle_type)
                force_magnitude = interaction_strength * interaction / (distance ** 2)
                force = force_magnitude * (distance_vector / distance)

                # Apply equal and opposite forces to both particles
                total_force += force
                other.velocity -= force * 0.5  # Apply the force to the "other" particle

            # Update the current particle's velocity
            particle.velocity += total_force * 0.5

    def update(self, noise_strength=0.1, interaction_strength=0.1, influence_range=50, friction=0.01):
        """
        Update all particles for one time step.
        """
        self.apply_interactions(interaction_strength, influence_range)
        for particle in self.particles:
            particle.apply_noise(noise_strength)
            particle.move(self.boundary, friction)

    def visualize(self, screen):
        """
        Visualize all particles using the Board class.
        """
        screen.fill((0, 0, 0))  # Clear screen
        for particle in self.particles:
            pygame.draw.circle(screen, particle.color, (int(particle.position[0]), int(particle.position[1])), 3)
        pygame.display.flip()
