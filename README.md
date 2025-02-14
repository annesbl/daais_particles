## daais_particles


# Wichtige Klassen:

Particle:

Repräsentiert ein einzelnes Partikel.
Enthält Attribute wie:
- Position (x, y)
- Geschwindigkeit (vx, vy)
- Typ (z. B. ein Index für die Interaktionsmatrix)
* Methoden:
* Bewegung (move) basierend auf aktueller Geschwindigkeit.
* Berechnung von Kräften mit anderen Partikeln.

Particles (oder eine Sammlung von Partikeln):

Repräsentiert die gesamte Partikelmenge.
Verantwortlich für:
- Initialisierung einer Liste von Partikeln.
- Verwaltung von Interaktionen zwischen allen Partikeln.
- Aktualisierung aller Partikelpositionen pro Zeitschritt.

Board:

Repräsentiert das Spielfeld.
Verantwortlich für:
- Begrenzungen (z. B. Partikel dürfen nicht aus dem Spielfeld herausfallen oder "wrap around").
- Effiziente Nachbarschaftsberechnungen (z. B. durch Gitterpartitionen oder Quadtrees).

Simulation:

Führt die Hauptlogik der Simulation aus.
Verantwortlich für:
- Die Simulationsschleife (z. B. 60 Schritte/Sekunde).
- Aktualisierung aller Partikel.
- Visualisierung und Parameteränderungen.
