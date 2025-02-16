#imports
import numpy as np
from scipy.spatial import cKDTree

class KDTree():
    #build a KD tree to find the nearest neighbors
    def initialise_tree(particle_array):
        tree = cKDTree(particle_array)
        return tree
    
    
class Interactions():
    #the total force between two particles
    def total_force(p1, p2, interaction_matrix):
        """
        Calculate the total force between two particles, including push and pull components.
        The forces depend on the particle types.
        Parameters:
        - p1, p2: Particles involved in the interaction.
        - pull_matrix: Dict defining pull force strengths based on particle types.
        - push_matrix: Dict defining push force strengths based on particle types.
        Returns:
        - total_force: Force vector acting on p1 due to p2.
        """
        pull_force = Interactions.pull_force(p1, p2, interaction_matrix)
        push_force = Interactions.push_force(p1, p2, interaction_matrix)
        return pull_force + push_force
    
    #the pull force between two particles
    def pull_force(p1, p2, interaction_matrix):
        distance = np.linalg.norm(p2.position - p1.position)
        if distance == 0:
            return np.zeros_like(p1.position)
        # Get pull strength from the matrix
        type_pair = (p1.particle_type, p2.particle_type)
        strength = interaction_matrix.get(type_pair, 0)
        # Pull force decreases with distance (e.g., inverse square)
        force_magnitude = strength / (distance**2)
        direction = (p2.position - p1.position) / distance
        return force_magnitude * direction
    
    #the push force between two particles
    def push_force(p1, p2, interaction_matrix):
        """
        Calculate the push force between two particles based on particle types.
        """
        distance = np.linalg.norm(p2.position - p1.position)
        if distance == 0 or distance > 1:  # Ignore if too far
            return np.zeros_like(p1.position)
        # Get push strength from the matrix
        type_pair = (p1.particle_type, p2.particle_type)
        strength = interaction_matrix.get(type_pair, 0)
        # Push force increases as particles get closer (e.g., inverse square)
        force_magnitude = -strength / (distance**2)
        direction = (p2.position - p1.position) / distance
        return force_magnitude * direction
class Implementation():
    #find the nearest particles, calculate the forces and return updated placements
    def update_particles(tree, influence_range,  particles, interaction_matrix, sim_area, friction):
        """
        Update particles by finding neighbors, calculating forces, and adjusting positions.
        Parameters:
        - tree: KD-tree built from the current particle positions.
        - particles: List of Particle objects.
        - influence_range: Radius for neighbor influence.
        - sim_area: [width, height] of the simulation area.
        - friction: Friction coefficient for velocity reduction.
        - pull_matrix: Dict defining pull force strengths based on particle types.
        - push_matrix: Dict defining push force strengths based on particle types.
        Returns:
        - updated_particles: List of updated Particle objects.
        """
        updated_particles = []
        for i, particle in enumerate(particles):
            # Find neighbors within the influence range
            neighbors_idx = tree.query_ball_point(particle.position, influence_range)
            total_force = np.zeros_like(particle.position)
            for idx in neighbors_idx:
                if idx != i:  # Skip self-interaction
                    total_force += Interactions.total_force(
                        particle, particles[idx], interaction_matrix, interaction_matrix
                    )
            
            # Apply force to velocity
            particle.velocity += total_force * 0.01  # Adjust time step as needed
            particle.move(sim_area, friction)  # Update position based on velocity
            updated_particles.append(particle)
        return updated_particles
