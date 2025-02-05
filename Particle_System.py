import random
import pygame
import numpy as np
from Particles import Particle
from interaction_class import KDTree, Implementation

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
            position = [np.random.uniform(0, boundary[0]), np.random.uniform(0, boundary[1])]
            velocity = [np.random.uniform(-1, 1), np.random.uniform(-1, 1)]
            particle_type = np.random.choice(list(types.keys()))
            color = types[particle_type]
            particles.append(Particle(position, velocity, particle_type, color))
        return particles

    def update(self, noise_strength=0.1, influence_range=50, friction=0.01):
        """
        Update particles by applying interactions and noise.

        Parameters:
        - noise_strength (float): Random noise added to particle velocity.
        - influence_range (float): Maximum distance for particle interaction.
        - friction (float): Friction applied to particle movement.
        """
        # Extract particle positions for KDTree
        particle_positions = [particle.position for particle in self.particles]

        # Build KDTree for neighbor searches
        kdtree = KDTree.initialise_tree(particle_positions)

        # Use the Implementation class to update particles
        self.particles = Implementation.update_particles(
            tree=kdtree,
            influence_range=influence_range,
            particles=self.particles,
            interaction_matrix=self.interaction_matrix,
            sim_area=self.boundary,
            friction=friction
        )

        # Apply random noise to all particles
        for particle in self.particles:
            particle.apply_noise(noise_strength)
