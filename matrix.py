import numpy as np

class InteractionMatrix:
    def __init__(self, types):   #initialisiert interaktionsmatrix
        self.types = types  #liste der Partikeltypen (diese typen definieren dimensionen der matrix)
        self.matrix = self._initialize_matrix()   #erstellt und speichert matrix mit zufälligen wertenzw -1 und 1

    def _initialize_matrix(self):   #erstellt quadratische matrix basierend auf anzahl der typen (jeder eintrag repräsentiert stärke der interaktion zw typen)
        size = len(self.types)   #größe der matrix = anzahl der typen
        return np.random.uniform(-1, 1, (size, size))  #Erstellt eine quadratische Matrix der Größe (size x size) mit zufälligen Werten im Bereich [-1, 1].
                                                       #Positive Werte bedeuten Anziehung, negative Abstoßung.

    def get_interaction(self, type1, type2):   #gibt interaktionsstrke zw zwei typen zurück
        idx1 = self.types.index(type1)   #index des ersten typen
        idx2 = self.types.index(type2)   #index des zweiten typen
        return self.matrix[idx1, idx2]   #gibt wert aus matrix zurück der die interaktion zw den beiden typen repräsentiert