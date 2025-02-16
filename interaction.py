#imports
import numpy as np
from scipy.spatial import cKDTree
from numba import jit




class KDTree():
    #build a KD tree to find the nearest neighbors
    def initialise_tree(particle_array):
        tree = cKDTree(particle_array) #Creates a KD-tree for nearest neighbor search
        return tree
    
    


class Interactions():
  # Calculates the total force between two particles
    def total_force(p1, particles, interaction_matrix, tree, radius):
        """
        Calculate the total force between two particles, including both push and pull components.
        The forces depend on the particle types.
        
        Parameters:
        - p1: The particle for which the total force is being calculated.
        - particles: The list of all particles in the system.
        - interaction_matrix: A matrix that stores the interaction strengths between different particle types.
        - tree: A cKDTree data structure that stores the particle positions for efficient neighbor searching.
        - radius: The radius within which the particles affect each other.
        
        Returns:
        - force: The force vector acting on p1 due to all neighboring particles within the specified radius.
        """
        # Initialize the total force as a zero vector
        force = np.zeros_like(p1.position)
        
        # Get the indices of particles that are within the interaction radius of p1
        neighbors_idx = tree.query_ball_point(p1.position, radius)  # Only particles within the radius

        # Loop over all neighboring particles
        for idx in neighbors_idx:
            p2 = particles[idx]
            
            # Skip the interaction with itself (no self-interaction)
            if p1 is not p2:
                # Calculate the vector from p1 to p2 and the distance between the particles
                distance_vector = p2.position - p1.position
                distance = np.linalg.norm(distance_vector)

                # Call the determine_force method to calculate the force between p1 and p2, 
                # and add it to the total force acting on p1
                force += Interactions.determine_force(p1, p2, interaction_matrix, distance_vector, distance)

        # Return the total force acting on p1
        return force



   ## Calculate the force between two particles
    def determine_force(p1, p2, interaction_matrix, distance_vector, distance):
        # If the distance between the particles is zero, return a zero vector (no force)
        if distance == 0:
            return np.zeros_like(p1.position)

        # Get the interaction strength between the two particle types from the interaction matrix
        type_pair = p1.particle_type, p2.particle_type
        strength = interaction_matrix.get_interaction(type_pair)
        
        # Calculate the magnitude of the force based on the inverse square law (strength / distance^2)
        force_magnitude = strength / (distance ** 2)
        
        # Normalize the direction of the force (unit vector in the direction of the distance vector)
        direction = distance_vector / distance
        
        # Return the force as the magnitude times the direction
        return force_magnitude * direction


class Implementation():
    #find the nearest particles, calculate the forces and return updated placements
    def update_particles(self, tree, influence_range,  particles, interaction_matrix, sim_area, friction):
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
            total_force = Interactions.total_force(
                particle, particles, interaction_matrix, tree, influence_range
            )

            # Apply force to velocity
            particle.velocity += total_force * 0.01  #Adjusts the velocity based on the time step
            particle.move(sim_area, friction)  #Update position based on velocity and position
            updated_particles.append(particle)

        return updated_particles
