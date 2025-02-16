import pygame
import time
from ParticleSystem import ParticleSystem
from Board import Board
from InteractionMatrix import InteractionMatrix

class Simulation:
    """Simuliert ein Partikelsystem mit verschiedenen Partikeltypen und Interaktionsregeln."""
    
    def __init__(self, width, height, particle_count, particle_types):
        """
        Initialisiert die Simulation.
        
        :param width: Breite des Fensters
        :param height: Höhe des Fensters
        :param particle_count: Anzahl der Partikel
        :param particle_types: Liste der verschiedenen Partikeltypen
        """
        self.width = width
        self.height = height
        self.running = True  # Steuert die Hauptschleife der Simulation
        self.paused = False  # Pausenstatus der Simulation
        self.frame_count = 0
        self.start_time = time.perf_counter()
        self.last_time = self.start_time

        # Initialisierung der Simulationselemente
        self.clock = pygame.time.Clock()  # Pygame-Uhr zur FPS-Steuerung
        self.interaction_matrix = InteractionMatrix(particle_types)  # Interaktionsmatrix der Partikeltypen
        self.particle_system = ParticleSystem(
            particle_count, (width, height), {ptype: None for ptype in particle_types}, self.interaction_matrix
        )  # Partikelsystem mit vordefinierten Regeln
        self.board = Board(width, height)  # Zeichenfläche für die Simulation

    def run(self):
        """Startet die Simulationsschleife."""
        while self.running:
            self.handle_events()  # Eingaben verarbeiten
            if not self.paused:
                self.update()  # Partikelsystem aktualisieren
            self.render()  # Darstellung der Simulation
            self.manage_fps()  # FPS-Steuerung und Anzeige

    def handle_events(self):
        """Verarbeitet Benutzer-Eingaben wie Beenden oder Pausieren der Simulation."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fenster schließen
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # 'P' zum Pausieren/Fortsetzen
                    self.toggle_pause()
                elif event.key == pygame.K_q:  # 'Q' zum Beenden der Simulation
                    self.running = False

    def toggle_pause(self):
        """Schaltet zwischen Pause und Fortsetzung der Simulation um."""
        self.paused = not self.paused
        print("Simulation Paused!" if self.paused else "Simulation Resumed!")

    def update(self):
        """Aktualisiert das Partikelsystem basierend auf Interaktionen und physikalischen Parametern."""
        self.particle_system.update(
            noise_strength=0.1,  # Zufällige Bewegung
            interaction_strength=0.5,  # Einfluss der Partikel aufeinander
            influence_range=50,  # Maximaler Einflussradius
            friction=0.01  # Bewegungswiderstand
        )

    def render(self):
        """Zeichnet die aktuelle Partikelkonfiguration und aktualisiert die Anzeige."""
        self.board.draw_particles(self.particle_system.particles)  # Partikel zeichnen
        self.board.update_display()  # Anzeige aktualisieren

    def manage_fps(self):
        """Begrenzt die FPS auf 60 und gibt die aktuelle FPS-Rate aus."""
        self.frame_count += 1
        current_time = time.perf_counter()
        elapsed_time = current_time - self.last_time
        if elapsed_time > 1.0:  # FPS alle 1 Sekunde berechnen
            fps = self.frame_count / elapsed_time
            print(f"FPS: {fps:.2f}")
            self.frame_count = 0
            self.last_time = current_time

        self.clock.tick(60)  # Maximale FPS auf 60 begrenzen

if __name__ == "__main__":
    # Simulationsparameter
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 500
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Simulation initialisieren und starten
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)
    simulation.run()

    # Pygame beenden
    pygame.quit()
