import pygame
import numpy as np
from particle_system import ParticleSystem
from board import Board
from matrix import InteractionMatrix

class Simulation:
    def __init__(self, width, height, particle_count, particle_types, interaction_matrix):
            self.width = width
            self.height = height
            self.running = True
            
            custom_interactions = {
            ("A", "B"): 1.0,   #A zieht B an
            ("A", "C"): -1.0,  #A stößt C ab
            ("B", "C"): 0.5,   #B zieht C schwach an
            ("D", "A"): -1.5,  #D stößt A stark ab
            }
        
            self.interaction_matrix = interaction_matrix
        
            self.particle_system = ParticleSystem(
            particle_count, (width, height), {ptype: None for ptype in particle_types}, self.interaction_matrix
            )
        
            self.board = Board(width, height)
        
    def run(self):
        while self.running:
                self.handle_events()
                self.update()
                self.render()
        
            
    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                
    def update(self):
        self.particle_system.update(
                noise_strength=0.1, influence_range=50, friction=0.01
            )
    
    def render(self):
        self.board.draw_particles(self.particle_system.particles)
        self.board.update_display()


if __name__ == "__main__":
    #Simulation parameters
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 300
    PARTICLE_TYPES = ["A", "B", "C", "D"]
    
    custom_interactions = {
        ("A", "B"): 0.0,
        ("A", "C"): 0.0,
        ("B", "C"): 0.0,
        ("D", "A"): 0.0,
        ("A", "A"): -100.0,
        ("B", "B"): 0.0,
        ("C", "C"): 0.0,
        ("D", "D"): 0.0,
    }
    interaction_matrix = InteractionMatrix(["A", "B", "C", "D"], custom_interactions)


    #Initialize and run the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES, interaction_matrix)
    simulation.run()
