# Particle Simulation using Pygame & KD-Tree
 
This project simulates particle interactions using **Pygame** for visualization and **KD-Tree** for efficient neighbor searches. It supports different particle types with attraction/repulsion interactions.

## 🌟 Features
- **Multiple Particle Types (A, B, C, D)**
- **Custom Interaction Matrix** for defining attraction/repulsion forces
- **KD-Tree Optimization** for efficient nearest-neighbor search
- **Real-Time Particle Movement & Rendering**
- **Toroidal Wrapping Boundaries** (Particles wrap around the screen)
- **Unit Tests for Core Components** (Particle System)

---

## 🏗️ Code 

📂 daais_particles 
│── 📜 README.md # Project Documentation 
│── 📜 requirements.txt # Required dependencies 
│── 📜 .gitignore # Ignoring unnecessary files 
│ ├── 📂 src # Main source code folder 
│ │── 📜 simulation.py # Main file to run the simulation 
│ │── 📜 particle_system.py # Handles particle updates & interactions 
│ │── 📜 particles.py # Particle class definition 
│ │── 📜 board.py # Handles Pygame visualization 
│ │── 📜 matrix.py # Defines interaction strengths 
│ │── 📜 interaction.py # Implements KD-Tree & forces calculations 
│ ├── 📂 tests # Unit tests 
│ │── 📜 test_particles.py # Unit tests for Particle class 
│ │── 📜 test_particle_system.py # Unit tests for ParticleSystem 
│ │── 📜 test_simulation.py # Integration tests 
│ └── 📂 assets # (Optional) Store assets like images


---

## 🚀 Installation & Setup
### ** 1 Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, install required libraries:

pip install -r requirements.txt

### ** 2 Run the Simulation**
Execute the following command:
python src/simulation.py

---

🔧 How the Code Works
🔹 1. simulation.py
Initializes the particle system and interaction matrix.
Runs the Pygame loop to render moving particles.

🔹 2. particle_system.py
Generates random particles with initial positions & velocities.
Uses KD-Tree for efficient neighbor searches.
Updates particle positions based on interactions & friction.

🔹 3. particles.py
Defines the Particle class, including:
Position, velocity, and size.
Methods to move particles and apply noise/randomness.

🔹 4. interaction.py
Implements KD-Tree for neighbor search.
Computes attraction/repulsion forces using a custom interaction matrix.

🔹 5. matrix.py
Defines interaction strengths between particle types.
Supports custom attraction/repulsion rules.

🔹 6. board.py
Handles Pygame visualization.
Renders particles and updates frames.

---

🧪 Running Unit Tests

To run tests, use:

python -m unittest discover tests/

---

⚡ Example Usage

Adjust Particle Count
Modify simulation.py:

PARTICLE_COUNT = 1000  # Increase for more particles

---

📌 Notes
This project is optimized using KD-Tree for large-scale simulations.
Pygame must be installed to visualize particles.

---

📜 License
This project is open-source and available under the MIT License.

