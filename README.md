#Heading 1
Particle Life Simulator

#Heaign 2
Group D

A dynamic particle simulation demonstrating emergent behavior through biology-inspired interaction rules.

#Heading 2
Table of Contents

Overview
Features
Installation and Setup
Code Structure


Overview
This project simulates particle interactions using **Pygame** for visualization and **KD-Tree** for efficient neighbor searches. It supports different particle types with attraction/repulsion interactions.

## 🌟 Features
- **Multiple Particle Types (A, B, C, D)**
- **Custom Interaction Matrix** for defining attraction/repulsion forces
- **KD-Tree Optimization** for efficient nearest-neighbor search
- **Real-Time Particle Movement & Rendering**
- **Toroidal Wrapping Boundaries** (Particles wrap around the screen)
- **Unit Tests for Core Components** (Particle System)

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
- Initializes the particle system and interaction matrix.
- Runs the Pygame loop to render moving particles.

🔹 2. particle_system.py
- Generates random particles with initial positions & velocities.
- Uses KD-Tree for efficient neighbor searches.
- Updates particle positions based on interactions & friction.

🔹 3. particles.py
- Defines the Particle class, including:
- Position, velocity, and size.
- Methods to move particles and apply noise/randomness.

🔹 4. interaction.py
- Implements KD-Tree for neighbor search.
- Computes attraction/repulsion forces using a custom interaction matrix.

🔹 5. matrix.py
- Defines interaction strengths between particle types.
- Supports custom attraction/repulsion rules.

🔹 6. board.py
- Handles Pygame visualization.
- Renders particles and updates frames.

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

