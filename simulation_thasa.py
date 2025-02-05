import pygame
import time
from ParticleSystem import ParticleSystem
from Board import Board
from InteractionMatrix import InteractionMatrix

class Simulation:
    def __init__(self, width, height, particle_count, particle_types):
        self.width = width
        self.height = height
        self.running = True
        self.paused = False
        self.frame_count = 0
        self.start_time = time.perf_counter()
        self.last_time = self.start_time

        # Initialize components
        self.clock = pygame.time.Clock()
        self.interaction_matrix = InteractionMatrix(particle_types)
        self.particle_system = ParticleSystem(
            particle_count, (width, height), {ptype: None for ptype in particle_types}, self.interaction_matrix
        )
        self.board = Board(width, height)

    def run(self):
        while self.running:
            self.handle_events()
            if not self.paused:
                self.update()
            self.render()
            self.manage_fps()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause/unpause on 'P'
                    self.toggle_pause()
                elif event.key == pygame.K_q:  # Quit on 'Q'
                    self.running = False

    def toggle_pause(self):
        """Toggle pause state."""
        self.paused = not self.paused
        print("Simulation Paused!" if self.paused else "Simulation Resumed!")

    def update(self):
        """Update particle system."""
        self.particle_system.update(
            noise_strength=0.1, interaction_strength=0.5, influence_range=50, friction=0.01
        )

    def render(self):
        """Render the current state of the simulation."""
        self.board.draw_particles(self.particle_system.particles)
        self.board.update_display()

    def manage_fps(self):
        """Manage FPS and print FPS every second."""
        self.frame_count += 1
        current_time = time.perf_counter()
        elapsed_time = current_time - self.last_time
        if elapsed_time > 1.0:  # Update FPS once per second
            fps = self.frame_count / elapsed_time
            print(f"FPS: {fps:.2f}")
            self.frame_count = 0
            self.last_time = current_time

        # Limit to 60 FPS
        self.clock.tick(60)


if __name__ == "__main__":
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 500
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Initialize and run the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)
    simulation.run()


    pygame.quit()
