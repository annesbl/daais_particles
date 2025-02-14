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

    def calculate_force(self, particle1, particle2):   #berechnet kraft zw zwei partikeln basierend auf interaktionsstärke und abstand
        
        interaction_strength = self.get_interaction(particle1.particle_type, particle2.particle_type)   #interaktionsstärke zw den beiden typen
        distance_vector = np.array(particle2.position) - np.array(particle1.position)   #berechnet vektor zw den beiden partikeln
        distance = np.linalg.norm(distance_vector)   #berechnet abstand (länge des vektors) zw den beiden partikeln
        if distance == 0 or distance > particle1.max_influence:     #Vermeidet Probleme:
                                                                    # - Wenn die Partikel exakt auf derselben Position sind (distance = 0), wird keine Kraft berechnet (sie stoßen sich nicht ab)(division durch 0)
                                                                    # - Wenn der Abstand größer ist als der maximale Einflussradius von particle1, wird keine Kraft berechnet (sie sind zu weit auseinander)
            return np.array([0, 0])  
        force = (interaction_strength / distance ** 2) * distance_vector   #berechnet kraft zw den beiden partikeln mit formel F = (k / r^2) * r (inverse quadratische abstandsabhängigkeit) kraft nimmt quadratisch mit der entfernung ab (abstand ^2 im nenner)
        return force   #gibt kraft als vektor zurück (pos anziehung, neg abstoßung)