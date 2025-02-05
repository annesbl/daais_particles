# Test Simulation File
import pygame
from Simulation_V2 import Simulation
from board import Board
from matrix import InteractionMatrix
from Particle_System import ParticleSystem
from Particles import Particle
from interaction_class import KDTree, Interactions, Implementation

def main():
    # Define Simulation Parameters
    WIDTH, HEIGHT = 900, 700
    PARTICLE_COUNT = 100  # Reduced particle count for testing
    PARTICLE_TYPES = ["A", "B", "C", "D"]  # Define particle types
    
    # Initialize Simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)
    
    # Test Particle Initialization
    print("Particles Initialized:")
    for particle in simulation.particle_system.particles[:10]:  # Show first 10 particles
        print(f"Type: {particle.particle_type}, Position: {particle.position}, Velocity: {particle.velocity}")
    
    # Run Simulation
    print("Starting simulation...")
    simulation.run()
    print("Simulation ended.")

if __name__ == "__main__":
    main()
