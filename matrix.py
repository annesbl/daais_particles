import numpy as np

class InteractionMatrix:
    def __init__(self, types):
        self.types = types  
        self.matrix = self._initialize_matrix()

    def _initialize_matrix(self):
       
        size = len(self.types)
        return np.random.uniform(-1, 1, (size, size))  

    def get_interaction(self, type1, type2):
        
        idx1 = self.types.index(type1)
        idx2 = self.types.index(type2)
        return self.matrix[idx1, idx2]

    def calculate_force(self, particle1, particle2):
        
        interaction_strength = self.get_interaction(particle1.particle_type, particle2.particle_type)
        distance_vector = np.array(particle2.position) - np.array(particle1.position)
        distance = np.linalg.norm(distance_vector)
        if distance == 0 or distance > particle1.max_influence:
            return np.array([0, 0])  
        force = (interaction_strength / distance ** 2) * distance_vector
        return force