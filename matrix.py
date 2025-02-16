import numpy as np

class InteractionMatrix:
    def __init__(self, types, custom_interactions=None):   #initialisiert interaktionsmatrix
        self.types = types  #liste der Partikeltypen (diese typen definieren dimensionen der matrix)
        self.matrix = self._initialize_matrix(custom_interactions)   #erstellt und speichert matrix mit zufälligen wertenzw -1 und 1

    def _initialize_matrix(self, custom_interactions):   #erstellt quadratische matrix basierend auf anzahl der typen (jeder eintrag repräsentiert stärke der interaktion zw typen)
        size = len(self.types)   #größe der matrix = anzahl der typen
        matrix = np.zeros((size, size))  #Erstellt eine quadratische Matrix der Größe (size x size) mit zufälligen Werten im Bereich [-1, 1].
        
        if custom_interactions:
            for (type1, type2), value in custom_interactions.items():
                idx1 = self.types.index(type1)
                idx2 = self.types.index(type2)
                matrix[idx1, idx2] = value
                matrix[idx2, idx1] = value 
        else:
            matrix = np.random.uniform(-1, 1, (size, size))#Positive Werte bedeuten Anziehung, negative Abstoßung.
        return matrix
    
    
    def get_interaction(self, type_pair):   #gibt interaktionsstärke zw zwei typen zurück
        type1, type2 = type_pair            #gibt interaktionsstrke zw zwei typen zurück
        idx1 = self.types.index(type1)   #index des ersten typen
        idx2 = self.types.index(type2)   #index des zweiten typen
        return self.matrix[idx1, idx2]   #gibt wert aus matrix zurück der die interaktion zw den beiden typen repräsentiert