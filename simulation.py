import pygame
from particle_system import ParticleSystem
from board import Board
from matrix import InteractionMatrix

class Simulation:
    def __init__(self, width, height, particle_count, particle_types):
            self.width = width
            self.height = height
            self.running = True
        
            self.interaction_matrix = InteractionMatrix(particle_types)
        
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
    # Simulation parameters
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 500
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Initialize and run the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)
    simulation.run()
