# Test Simulation File
import pygame
import numpy as np
from simulation import Simulation
from Particle_System import ParticleSystem
from Particles import Particle
from matrix import InteractionMatrix

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
    interaction_matrix = InteractionMatrix(PARTICLE_TYPES)
    interaction_matrix.matrix = np.zeros((len(PARTICLE_TYPES), len(PARTICLE_TYPES)))
    
    # Assign custom rules
    for (type1, type2), value in custom_rules.items():
        idx1 = PARTICLE_TYPES.index(type1)
        idx2 = PARTICLE_TYPES.index(type2)
        interaction_matrix.matrix[idx1, idx2] = value

    # Initialize and run the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)
    simulation.run()

if __name__ == "__main__":
    main()
