# Test Simulation File
import pygame
from simulation import Simulation
from board import Board
from matrix import InteractionMatrix
from Particle_System import ParticleSystem
from Particles import Particle
from interaction_class import KDTree, Interactions, Implementation

def main():
    # Simulation parameters
    WIDTH, HEIGHT = 900, 700
    PARTICLE_COUNT = 1000  # Set particle count to 1000
    PARTICLE_TYPES = ["A", "B", "C", "D"]  # Define particle types

    # Define specific interaction rules
    custom_rules = {
        ("A", "B"): 1.0,    # A attracts B
        ("B", "C"): -1.0,   # B repels C
        ("C", "D"): 0.5,    # C attracts D
        ("D", "A"): 0.0,    # D has no interaction with A
    }

    # Initialize the interaction matrix with custom rules
    interaction_matrix = InteractionMatrix(PARTICLE_TYPES, custom_rules)

    # Initialize the simulation with the specified parameters
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES, interaction_matrix)

    # Run the simulation
    simulation.run()

if __name__ == "__main__":
    main()

