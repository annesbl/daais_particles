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
    def total_force(particle1, particle2):
        pass
    #the pull force between two particles
    def pull_force(particle1, particle2):
        pass
    #the push force between two particles
    def push_force(particle1, particle2):
        pass

class Implementation():
    #find the nearest particles, calculate the forces and return updated placements
    def update_particles(tree, influence_range,  particle_array, forces):
        updated_positions = np.zeros_like(particle_array)
        for i, particle in enumerate(particle_array):
            neighbors = tree.query_ball_point(particle.position, influence_range)
            total_force = forces