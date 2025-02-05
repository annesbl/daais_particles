from simulation import Simulation

if __name__ == "__main__":
    # Simulation parameters
    WIDTH = 800
    HEIGHT = 600
    PARTICLE_COUNT = 500
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Initialize the simulation
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)

    # Run the simulation
    simulation.run()
