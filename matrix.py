import numpy as np

class InteractionMatrix:
    def __init__(self, types, custom_interactions=None): 
        """
        Initializes the interaction matrix with particle types and optionally custom interaction values
        """  
        self.types = types  #List of particle types
        self.matrix = self._initialize_matrix(custom_interactions)  #Initializes the interaction matrix

    
    def _initialize_matrix(self, custom_interactions):   #erstellt quadratische matrix basierend auf anzahl der typen (jeder eintrag repräsentiert stärke der interaktion zw typen)
        size = len(self.types)   #Size of the matrix= number of types
        matrix = np.zeros((size, size))  #Creates a square matrix for interactions
        
        if custom_interactions:
            #Assigns custom interaction values if provided
            for (type1, type2), value in custom_interactions.items():
                idx1 = self.types.index(type1)
                idx2 = self.types.index(type2)
                matrix[idx1, idx2] = value
                matrix[idx2, idx1] = value 
        else:
            matrix = np.random.uniform(-1, 1, (size, size)) #Random interactions between -1 and 1
        return matrix
    
    
    def get_interaction(self, type_pair):  
        """
        Retrieves the interaction strength between the given pair of particle types
        """ 
        type1, type2 = type_pair            
        idx1 = self.types.index(type1)   
        idx2 = self.types.index(type2)   
        return self.matrix[idx1, idx2]   #Returns interaction strength between the two types