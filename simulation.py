import pygame
import numpy as np
from particle_system import ParticleSystem
from board import Board
from matrix import InteractionMatrix



class Simulation:
    def __init__(self, width, height, particle_count, particle_types, interaction_matrix):
            self.width = width
            self.height = height
            self.running = True  #Flag to control the simulation's run state
            self.interaction_matrix = interaction_matrix  #Assigns the provided interaction matrix
            
            #Initializes the particle system with the given parameters
            self.particle_system = ParticleSystem(
            particle_count, (width, height), {ptype: None for ptype in particle_types}, self.interaction_matrix
            )
            #Initializes the board for rendering the simulation
            self.board = Board(width, height)
        
    
    def run(self):
        """
        Main loop that runs the simulation
        """
        while self.running:
                self.handle_events()  #Handles user inputs or quit event
                self.update()  #Updates the simulation state (particles, interactions)
                self.render()  #Renders the updated particle system on the screen

        
    def handle_events(self):
        """
        Checks for user input events (e.g., quit request)
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  #Stops the simulation if the user closes the window

                
    def update(self):
        """
        Updates the particle system with the given parameters
        """
        self.particle_system.update(
                noise_strength=0.1, influence_range=50, friction=0.01
            )
    
    def render(self):
        """
        Draws the particles on the screen and updates the display
        """
        self.board.draw_particles(self.particle_system.particles)
        self.board.update_display()  #Refreshes the display to show the new state


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
