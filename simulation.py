import pygame
from Particle_System import ParticleSystem
from board import Board
from matrix import InteractionMatrix

class Simulation: 
    def __init__(self, width, height, particle_count, particle_types, interaction_matrix):
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
        self.board.draw_particles_with_trails(self.particle_system.particles)
        self.board.update_display()


if __name__ == "__main__":
    # Simulation parameters
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 1000
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Define specific interaction rules
    custom_rules = {
        ("A", "B"): 1.0,    # A attracts B
        ("B", "C"): -1.0,   # B repels C
        ("C", "D"): 0.5,    # C attracts D
        ("D", "A"): 0.0,    # D has no interaction with A
    }

    # Initialize the interaction matrix with custom rules
    interaction_matrix = InteractionMatrix(PARTICLE_TYPES, custom_rules)

    # Initialize and run the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES, interaction_matrix)
    simulation.run()
