import time
from particleSystem import particleSystem
from board import board

class Simulation:
    """
    The Simulation class manages the overall particle simulation process.
    """
    def __init__(self, particle_count=100, boundaries=(800, 600), time_step=0.1, noise_strength=0.01, gui_enabled=True):
        """
        Initialize the Simulation instance.

        Args:
            particle_count (int): Number of particles in the simulation.
            boundaries (tuple): Tuple (width, height) for the simulation boundary.
            time_step (float): Duration of a simulation step.
            noise_strength (float): Strength of added noise/randomness to particles.
            gui_enabled (bool): Whether the GUI visualization is enabled.
        """
        self.particles = []  # All particles in the simulation
        self.time_step = time_step  # Simulation time step duration
        self.noise_strength = noise_strength  # Noise strength for randomness
        self.gui_enabled = gui_enabled  # GUI visualization flag
        self.frame_count = 0  # Frame counter
        self.particlesystem = particleSystem()
        self.board = board(width=boundaries[0], height=boundaries[1], visualizer=None)  # Visualization board
        
        # Initialize particles using the particleSystem
        self.particlesystem.initialize_particles(count=particle_count, boundaries=boundaries, type="random")
        self.particles = self.particlesystem.particles

    def run(self, steps=1000):
        """
        Start the simulation loop.

        Args:
            steps (int): Number of steps to simulate.
        """
        print("Starting simulation...")
        for step in range(steps):
            self.frame_count += 1
            print(f"Frame {self.frame_count}")
            
            # Update particle positions
            self.update_particles()
            
            # Apply interaction forces (placeholder logic)
            self.apply_interactions()
            
            # Render the current state
            if self.gui_enabled:
                self.render_frame()
            
            # Sleep to maintain simulation speed
            time.sleep(self.time_step)

        print("Simulation completed.")

    def update_particles(self):
        """
        Update the positions and states of all particles.
        """
        print("Updating particles...")
        self.particlesystem.update(self.noise_strength)

    def apply_interactions(self):
        """
        Apply interaction forces between particles.
        """
        print("Applying interactions...")
        # Placeholder: Here you would calculate forces using InteractionMatrix
        # For example:
        # self.interaction_matrix.calculate_forces(self.particles)
        pass

    def render_frame(self):
        """
        Render the current state of the particles on the board.
        """
        print("Rendering frame...")
        self.board.draw_particles(self.particles)
        self.board.update_display()

    def reset_simulation(self):
        """
        Reset the simulation to its initial state.
        """
        print("Resetting simulation...")
        self.frame_count = 0
        self.particlesystem.initialize_particles(count=len(self.particles), boundaries=(self.board.width, self.board.height), type="random")
        self.particles = self.particlesystem.particles

    def save_state(self, filename="simulation_state.json"):
        """
        Save the current state of the simulation to a file.

        Args:
            filename (str): The file to save the state to.
        """
        print("Saving simulation state...")
        state = {
            "frame_count": self.frame_count,
            "particles": [particle.serialize() for particle in self.particles]
        }
        with open(filename, "w") as file:
            import json
            json.dump(state, file, indent=4)
        print(f"State saved to {filename}")
