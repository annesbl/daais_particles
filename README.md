# Particle Life Simulator

## Introduction

The **Particle Life Simulator** is a dynamic, biology-inspired particle simulation that models the interactions between different types of particles. Using real-time rendering with Pygame and efficient computations with KD-Tree, this simulation allows you to observe how particles behave based on attraction and repulsion forces. By utilizing a custom interaction matrix, this simulator provides flexibility in controlling how different particle types interact with one another.

## Project Overview

This project demonstrates emergent behavior through simple particle interactions, simulating physics principles such as attraction, repulsion, and friction. Particles can be of various types, and their behavior is governed by a custom interaction matrix, which allows for fine-tuning of their forces based on type-pair interactions. The simulation is optimized for performance with a KD-Tree implementation, ensuring efficient neighbor searches even when running with a large number of particles.

The system supports a variety of particle types (A, B, C, D) and interaction rules. The simulation environment uses **Pygame** for visualization and **NumPy** and **SciPy** for calculations and optimizations.

## Features

- **Multiple Particle Types**: Simulate different types of particles (A, B, C, D), each with its own behavior and interaction properties.
- **Custom Interaction Matrix**: Define attraction/repulsion strengths for particle interactions.
- **Efficient KD-Tree Optimization**: Perform fast neighbor searches for large numbers of particles, enhancing performance.
- **Real-Time Visualization**: Observe particle movements in real-time with Pygame rendering.
- **Toroidal Wrapping Boundaries**: Particles reappear on the opposite side of the simulation area when they reach the edge.
- **Unit Tests**: Core components of the simulation are covered by unit tests to ensure correctness.
- **Customization**: Easily adjust particle count, interaction strengths, and other parameters to see how the system behaves.

## Installation

To install the **Particle Life Simulator**, follow these steps:<br>

1. Clone the repository:<br>

bash<br>
git clone https://github.com/annesbl/daais_particles.git<br>
cd daais_particles<br>
Install the package:<br>
python -m pip install .<br>
Or, on macOS:<br>

python3 -m pip install .<br>
Install the required dependencies:<br>
pip install pygame numpy scipy<br>

## Usage

Adjust Particle Count
To change the number of particles, modify the PARTICLE_COUNT variable in simulation.py:

PARTICLE_COUNT = 1000  # Adjust this to change the number of particles
Running the Simulation<br>
Once you have configured your settings, you can run the simulation with:

python simulation.py<br>
This will open a Pygame window where you can watch the particles interact based on the interaction matrix.

## Project Architecture

The project is structured into several modules that handle different parts of the simulation:

daais_particles/<br>
├── particle_life/<br>
│   ├── Class_board.py              # Handles visualization<br>
│   ├── Class_particles.py         # Defines particle properties and movement<br>
│   ├── Class_simulation.py        # Contains the main simulation logic<br>
│   ├── Class_interaction.py       # Computes interaction forces and KD-Tree operations<br>
│   ├── Class_matrix.py            # Manages the interaction matrix<br>
│   ├── Class_particle_system.py   # Manages the particle system and updates<br>
├── tests/<br>
│   ├── test_board.py              # Unit tests for the board class<br>
│   ├── test_particles.py         # Unit tests for particle class<br>
│   ├── test_simulation.py        # Unit tests for simulation class<br>
│   ├── test_interaction.py       # Unit tests for interaction logic<br>
│   ├── test_matrix.py            # Unit tests for matrix class<br>
│   ├── test_particle_system.py   # Unit tests for the particle system<br>
├── README.md                     # Project documentation<br>
├── LICENSE                        # License file<br>


## Main Components
**simulation.py:** The entry point of the simulation. Initializes the particle system and interaction matrix, and runs the Pygame loop.<br>
**particle_system.py:** Manages the creation and updating of particles using the KD-Tree for efficient nearest-neighbor searches.<br>
**particles.py:** Defines the Particle class, which includes attributes like position, velocity, and type.<br>
**interaction.py:** Handles particle interaction logic, including force calculations using the custom interaction matrix and KD-Tree optimization.<br>
**matrix.py:** Contains the InteractionMatrix class, which defines interaction strengths between particle types and supports both custom and random interactions.<br>
**board.py:** Manages the Pygame window and rendering of particles.<br>

## Performance Optimization

The use of KD-Tree (implemented using scipy.spatial.cKDTree) significantly improves performance by allowing for efficient spatial querying of neighboring particles. This makes it feasible to simulate and visualize large numbers of particles (e.g., 1000+ particles) with minimal performance degradation.

In addition, the NumPy library is used for efficient numerical computations (like calculating distances and forces), ensuring that operations involving particle properties and interactions are fast and vectorized.

## Testing & CI

Unit tests are provided for core components of the project, ensuring that individual classes and methods behave as expected. The tests cover:

Particle movement (e.g., position updates, applying friction, and noise).
Interaction forces (e.g., correct calculation of attraction/repulsion forces based on the interaction matrix).
Particle system updates (e.g., ensuring that particles are correctly updated and that forces are applied properly).
To run the tests:

python -m unittest discover tests/

## Project Management

The project follows a modular approach, with separate classes handling distinct aspects of the simulation. This structure enables easy maintenance, testing, and potential extension of features. Additionally, all core functionalities are covered by unit tests to ensure correctness.

## Challenges & Lessons Learned

**Handling Large Numbers of Particles:** A key challenge in this simulation was optimizing performance when simulating large particle counts. Implementing the KD-Tree for fast neighbor searches was crucial for ensuring the system remained performant as the number of particles grew.<br>
**Tuning Interaction Strengths:** Defining a meaningful and balanced interaction matrix was another challenge. After experimenting with various values, we found that varying the interaction strengths allowed us to model different behaviors, like attraction and repulsion between different types of particles.<br>
**Visualization with Pygame:** While Pygame was useful for visualization, managing the rendering loop to ensure smooth updates at a high frame rate was challenging. We used pygame.time.Clock() to limit the frame rate to 60 FPS, which kept the simulation responsive.<br>

## Future Work

**Improved Performance for Large Simulations:** While KD-Tree optimization improves performance, the simulation could still benefit from further optimization, especially when working with larger particle systems.<br>
**Advanced Interaction Models:** Future versions could introduce more sophisticated interaction models, including additional forces or particle behaviors based on environmental factors (e.g., temperature or external fields).<br>
**User Interface for Parameter Adjustments:** A graphical user interface (GUI) would allow users to dynamically adjust parameters like particle count, interaction strength, and simulation speed during runtime.<br>
**Integration with Machine Learning:** It would be interesting to explore how machine learning algorithms could be used to model or predict particle behavior or interactions more accurately.

## Authors

Anne S. and Jule N. – Primary Developer and Project Leaders<br>
Amilin Binti S. and Thasarathakumar P.– Contributors and Developers

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
