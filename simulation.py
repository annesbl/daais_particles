import pygame
from ParticleSystem import ParticleSystem
from Board import Board
from InteractionMatrix import InteractionMatrix

class Simulation:
    def __init__(self, width, height, particle_count, particle_types):
        """
        Initialize the Simulation class.

        Parameters:
        - width (int): Width of the simulation area.
        - height (int): Height of the simulation area.
        - particle_count (int): Number of particles to simulate.
        - particle_types (list): List of particle types.
        """
        self.width = width
        self.height = height
        self.running = True

        # Initialize the Interaction Matrix
        self.interaction_matrix = InteractionMatrix(particle_types)

        # Initialize the Particle System
        self.particle_system = ParticleSystem(
            particle_count, (width, height), {ptype: None for ptype in particle_types}, self.interaction_matrix
        )

        # Initialize the Board for visualization
        self.board = Board(width, height)

    def run(self):
        """
        Main simulation loop.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        """
        Handle user input events to allow quitting the simulation.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """
        Update the particle system for one simulation step.
        """
        self.particle_system.update(
            noise_strength=0.1, interaction_strength=0.5, influence_range=50, friction=0.01
        )

    def render(self):
        """
        Render the particle system using the Board.
        """
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
