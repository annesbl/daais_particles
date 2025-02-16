import numpy as np
import pytest
from matrix import InteractionMatrix  # 

def test_initialize_matrix_random():
    """Testet, ob die Interaktionsmatrix korrekt mit zufälligen Werten initialisiert wird."""
    types = ["A", "B", "C"]
    matrix = InteractionMatrix(types)

    assert matrix.matrix.shape == (3, 3)  # Die Matrix sollte quadratisch sein
    assert -1 <= matrix.matrix.min() <= 1  # Werte sollten im Bereich [-1, 1] liegen
    assert -1 <= matrix.matrix.max() <= 1

def test_initialize_matrix_custom():
    """Testet, ob die Matrix korrekt mit benutzerdefinierten Werten initialisiert wird."""
    types = ["A", "B", "C"]
    custom_interactions = {("A", "B"): 0.5, ("B", "C"): -0.7}
    
    matrix = InteractionMatrix(types, custom_interactions)

    assert matrix.get_interaction(("A", "B")) == 0.5
    assert matrix.get_interaction(("B", "A")) == 0.5  # Symmetrische Matrix
    assert matrix.get_interaction(("B", "C")) == -0.7
    assert matrix.get_interaction(("C", "B")) == -0.7
    assert matrix.get_interaction(("A", "C")) == 0  # Keine definierte Interaktion → Standardwert 0

def test_get_interaction():
    """Testet die get_interaction-Methode mit festen Werten."""
    types = ["A", "B"]
    custom_interactions = {("A", "B"): 0.8}
    matrix = InteractionMatrix(types, custom_interactions)

    assert matrix.get_interaction(("A", "B")) == 0.8
    assert matrix.get_interaction(("B", "A")) == 0.8
    assert matrix.get_interaction(("A", "A")) == 0  # Standardwert für nicht gesetzte Werte
    assert matrix.get_interaction(("B", "B")) == 0

def test_invalid_type():
    """Testet, ob ein Fehler ausgelöst wird, wenn ein unbekannter Typ abgefragt wird."""
    types = ["A", "B"]
    matrix = InteractionMatrix(types)

    with pytest.raises(ValueError):
        m
