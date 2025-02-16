# Particle Life Simulator

# Group E

A dynamic particle simulation demonstrating emergent behavior through biology-inspired interaction rules.

# Table of Contents

- [Overview](#-overview)
- [Features](#-🌟-features)
- [Installation and Setup](#-🚀-installation-&-setup)
- [Project Structure](#-project-structure)
- [Code Structure](#-🔧-code-structure)
- [License](#license)


## Overview
This project simulates particle interactions using **Pygame** for visualization and **KD-Tree** for efficient neighbor searches. It supports different particle types with attraction/repulsion interactions.

## Features
- **Multiple Particle Types (A, B, C, D)**
- **Custom Interaction Matrix** for defining attraction/repulsion forces
- **KD-Tree Optimization** for efficient nearest-neighbor search
- **Real-Time Particle Movement & Rendering**
- **Toroidal Wrapping Boundaries** (Particles wrap around the screen)
- **Unit Tests for Core Components** (Particle System)

## System Requirements 

✅ Python 3.8+
✅ Required Libraries: pygame, numpy, scipy

## 🚀 Installation & Setup

To install particle_life_simulator from a GitHub repository, run: 
```sh 
git clone https://github.com/annesbl/daais_particles.git
cd daais_particles
python -m pip install .
or on mac: python3 -m pip install 
```
Make sure you have Pygame and other dependencies installed:

```sh 
pip install pygame numpy scipy

```

## ⚡ How to use 

1. Adjust Particle Count Modify simulation.py:

```sh
PARTICLE_COUNT = 1000 # Increase for more particles
```

2. Run the Simulation
```sh 
python simulation.py

```

3. Pygame Window opens showing moving particles.

## Project Structure

```sh
daais_particles/
├── particle_life/
│   ├── Class_board.py                
│   ├── Class_particles.py           
│   ├── Class_simulation.py      
│   ├── Class_interaction.py
│   ├── Class_matrix.py
│   ├── Class_particle_system.py
├── tests/
│   ├── test_board.py                
│   ├── test_particles.py           
│   ├── test_simulation.py      
│   ├── test_interaction.py
│   ├── test_matrix.py
│   ├── test_particle_system.py     
├── README.md                       # Project documentation
├── LICENSE                         # License file
```

## 🔧 Code Structure
### 1. simulation.py
- Initializes the particle system and interaction matrix.
- Runs the Pygame loop to render moving particles.

### 2. particle_system.py
- Generates random particles with initial positions & velocities.
- Uses KD-Tree for efficient neighbor searches.
- Updates particle positions based on interactions & friction.

### 3. particles.py
- Defines the Particle class, including:
- Position, velocity, and size.
- Methods to move particles and apply noise/randomness.

### 4. interaction.py
- Implements KD-Tree for neighbor search.
- Computes attraction/repulsion forces using a custom interaction matrix.

### 5. matrix.py
- Defines interaction strengths between particle types.
- Supports custom attraction/repulsion rules.

### 6. board.py
- Handles Pygame visualization.
- Renders particles and updates frames.


## Running Tests 


## 🚀 Future Improvements 
✔️ Add GUI controls (adjust speed, interaction strength).
✔️ Improve performance for large particle counts.
✔️ Introduce new interaction rules dynamically.

## 📌 Notes
This project is optimized using KD-Tree for large-scale simulations.
Pygame must be installed to visualize particles.

## 📜 License
This project is open-source and available under the MIT License.

