#imports
import pygame
import numpy as np
from Particles import Particle
from Particle_System import ParticleSystem
from matrix import InteractionMatrix
from board import Board
from simulation import Simulation
from interaction_class import KDTree, Implementation

# Simulation parameters
WIDTH, HEIGHT = 800, 600
PARTICLE_COUNT = 500
PARTICLE_TYPES = {"A": (255, 0, 0), "B": (0, 255, 0), "C": (0, 0, 255), "D": (255, 255, 0)}
INFLUENCE_RANGE = 100
FRICTION = 0.01

# Initialize pygame
pygame.init()

# Create simulation area and display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation with KDTree and Interactions")

# Initialize components
interaction_matrix = InteractionMatrix(list(PARTICLE_TYPES.keys()))
particle_system = ParticleSystem(PARTICLE_COUNT, (WIDTH, HEIGHT), PARTICLE_TYPES, interaction_matrix)
board = Board(WIDTH, HEIGHT)

# Main simulation loop
running = True
while running:
    # Handle pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Extract particle positions for KDTree
    particle_positions = [particle.position for particle in particle_system.particles]
    kdtree = KDTree.initialise_tree(particle_positions)

    # Update particles using KDTree and interaction forces
    particle_system.particles = Implementation.update_particles(
        kdtree,
        INFLUENCE_RANGE,
        particle_system.particles,
        interaction_matrix,
        (WIDTH, HEIGHT),
        FRICTION
    )

    # Render updated particles on the board
    board.draw_particles(particle_system.particles)
    board.update_display()

pygame.quit()
