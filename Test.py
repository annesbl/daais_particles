import pygame
from Particles import Particle
from Particle_System import ParticleSystem

# Define particle types and interaction matrix
particle_types = {
    'A': (255, 0, 0),   # Red
    'B': (0, 255, 0),   # Green
    'C': (0, 0, 255),   # Blue
    'D': (255, 255, 0), # Yellow
}

interaction_matrix = {
    'A': {'A': 0, 'B': 1, 'C': -1, 'D': 0.5},
    'B': {'A': -1, 'B': 0, 'C': 1, 'D': -0.5},
    'C': {'A': 1, 'B': -1, 'C': 0, 'D': 0.2},
    'D': {'A': -0.5, 'B': 0.5, 'C': -0.2, 'D': 0},
}

# Initialize particle system
particle_count = 100
boundary = (800, 600)
system = ParticleSystem(particle_count, boundary, particle_types, interaction_matrix)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(boundary)
clock = pygame.time.Clock()

# Run the simulation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    system.update(noise_strength=0.2, interaction_strength=0.5, influence_range=50, friction=0.01)
    system.visualize(screen)
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()

