import pygame
from Particles import Particle
from Particle_System import ParticleSystem
from matrix import InteractionMatrix
from board import Board

# Simulation parameters
particle_count = 100  
boundary = (800, 600)  # Width, Height
particle_types = {
    "A": (255, 0, 0),   # Red
    "B": (0, 255, 0),   # Green
    "C": (0, 0, 255),   # Blue
    "D": (255, 255, 0)  # Yellow
}

# Initialize InteractionMatrix
interaction_matrix = InteractionMatrix(list(particle_types.keys()))

# Initialize Particle System and Board
particle_system = ParticleSystem(particle_count, boundary, particle_types, interaction_matrix)
board = Board(boundary[0], boundary[1])

# Main simulation loop
pygame.init()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    particle_system.update(noise_strength=0.2, interaction_strength=0.5, influence_range=100, friction=0.01)

    # Draw particles
    board.draw_particles(particle_system.particles)
    board.update_display()

pygame.quit()
