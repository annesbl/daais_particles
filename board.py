import pygame

class Board:
    def __init__(self, width, height):   #initalisierung mit paraetern für breite und höhe
        self.width = width   #speichert breite des Fensters
        self.height = height    #speichert höhe des Fensters
        
        # initialisierung von pygame und erstellung des Fensters
        pygame.init()   # startet pygame und initialisiert alle module
        self.screen = pygame.display.set_mode((width, height))   # erstellt ein fenster mit der größe width x height
        self.clock = pygame.time.Clock()   # Erstellt ein Clock-Objekt, das verwendet wird, um die Bildrate (Frames per Second, FPS) zu steuern.
        self.trail_surface = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a surface for trails with alpha support

    def draw_particles(self, particles):   # methode zum zeichnen der partikel
        self.screen.fill((0, 0, 0))  # macht hintergrund schwarz
        for particle in particles:   # iteriert durch liste der partikel und zeichnet jedes einzelne
            x, y = int(particle.position[0]), int(particle.position[1])   # konvertiert die position des partikels in integer
            color = self.get_color_by_type(particle.particle_type)    # ruft farbe der partikel ab, basierend auf dem typ
            pygame.draw.circle(self.screen, color, (x, y), 3)    # Zeichnet einen Kreis auf das Fenster:
                                                                 # - `self.screen`: Das Pygame-Fenster, in dem der Kreis gezeichnet wird.
                                                                 # - `color`: Die Farbe des Kreises.
                                                                 # - `(x, y)`: Die Position des Kreises (Mittelpunkt).
                                                                 # - `3`: Der Radius des Kreises in Pixeln.

        pygame.display.flip()   # aktualisiert das fenster mit den gezeichneten partikeln und änderungen
                                # ohne den werden änderungen nicht angezeigt

    def update_display(self):   # kontrolliert die bildrate des fensters damit nicht zu schnell
        self.clock.tick(60)     # wartet bis genügend zeit vergangen ist, um die bildrate auf 60 fps zu halten (also max 60 frames per second)
        
    def get_color_by_type(self, particle_type):   # methode um farbe der partikel basierend auf dem typ zu erhalten
        colors = {
            "A": (255, 0, 0),  # Red
            "B": (0, 255, 0),  # Green
            "C": (0, 0, 255),  # Blue
            "D": (255, 255, 0)  # Yellow
        }
        return colors.get(particle_type, (255, 255, 255))  # gibt farbe des partikels zurück, wenn der typ nicht in der liste ist, wird weiß zurückgegeben

    '''
    def draw_particles(self, particles):
        # Draw a semi-transparent background to create trails
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 10))  # Last value is alpha transparency
        self.screen.blit(overlay, (0, 0))
    
        for particle in particles:
            x, y = int(particle.position[0]), int(particle.position[1])
            color = self.get_color_by_type(particle.particle_type)
            pygame.draw.circle(self.screen, color, (x, y), 3)

        pygame.display.flip()
    '''

    def draw_particles_with_trails(self, particles):
        # Make the trail fade gradually
        self.trail_surface.fill((0, 0, 0, 10))  # Semi-transparent black overlay
        for particle in particles:
            x, y = int(particle.position[0]) % self.width, int(particle.position[1]) % self.height
            color = self.get_color_by_type(particle.particle_type)  # Ensure valid color for particle type
            pygame.draw.circle(self.trail_surface, color, (x, y), 3)  # Draw particle with radius 3
        self.screen.blit(self.trail_surface, (0, 0))  # Combine trail surface with the main screen
        pygame.display.flip()




    