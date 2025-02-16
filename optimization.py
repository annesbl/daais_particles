#imports
from simulation import Simulation
import cProfile


def your_function():
    # Simulation parameters
    WIDTH, HEIGHT = 800, 600
    PARTICLE_COUNT = 500
    PARTICLE_TYPES = ["A", "B", "C", "D"]

    # Simulation initialisieren
    simulation = Simulation(WIDTH, HEIGHT, PARTICLE_COUNT, PARTICLE_TYPES)

    # Profiling der run-Methode durchführen
    simulation.run()

# Profiling mit cProfile durchführen
profiler = cProfile.Profile()
profiler.enable()  # Profiling starten
your_function()
profiler.disable()  # Profiling stoppen

# Ergebnisse speichern
profiler.dump_stats('profiling_results.prof')
