import pygame
from ParticleSystem import ParticleSystem
from Board import Board
from InteractionMatrix import InteractionMatrix

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
