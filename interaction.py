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
  #calculates the total force between two particles
    def total_force(p1, particles, interaction_matrix, tree, radius):
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
        total_force = np.zeros_like(p1.position)
        neighbors_idx = tree.query_ball_point(p1.position, radius)  # Nur Partikel im Radius

        for idx in neighbors_idx:
            p2 = particles[idx]
            if p1 is not p2:  # Keine Selbst-Interaktion
                distance_vector = p2.position - p1.position
                distance = np.linalg.norm(distance_vector)

                # Übergabe von 'distance' zu den Methoden
                total_force += Interactions.pull_force(p1, p2, interaction_matrix, distance_vector, distance)
                total_force += Interactions.push_force(p1, p2, interaction_matrix, distance_vector, distance)

        return total_force


    ##the pull force between two particles
    @jit(nopython=True)  # JIT compilation (no parallelization needed for this one)
    def pull_force(p1, p2, interaction_matrix, distance_vector, distance):
        if distance == 0:
            return np.zeros_like(p1.position)

        type_pair = p1.particle_type , p2.particle_type
        strength = interaction_matrix.get_interaction(type_pair)
        force_magnitude = strength / (distance ** 2)
        direction = distance_vector / distance
        return force_magnitude * direction

    #the push force between two particles
    @jit(nopython=True)  # JIT compilation (no parallelization needed for this one)
    def push_force(p1, p2, interaction_matrix, distance_vector, distance):
        if distance == 0 or distance > 1:  # Begrenzung der Push-Kraft

            return np.zeros_like(p1.position)

        type_pair = p1.particle_type , p2.particle_type
        strength = interaction_matrix.get_interaction(type_pair)

        force_magnitude = -strength / (distance ** 2)
        direction = distance_vector / distance
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
