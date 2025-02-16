import pytest
import numpy as np
from your_module import InteractionMatrix  # Ersetze 'your_module' mit deinem Modulnamen

def test_initialize_matrix_random():
    """Testet, ob die zufällige Interaktionsmatrix korrekt initialisiert wird."""
    types = ["A", "B", "C"]
    matrix = InteractionMatrix(types)
    
    assert matrix.matrix.shape == (3, 3)
    assert -1 <= np.min(matrix.matrix) <= 1  # Werte müssen zwischen -1 und 1 liegen
    assert -1 <= np.max(matrix.matrix) <= 1

def test_initialize_matrix_custom():
    """Testet die Initialisierung mit benutzerdefinierten Interaktionen."""
    types = ["A", "B", "C"]
    custom_interactions = {("A", "B"): 0.5, ("B", "C"): -0.3}
    matrix = InteractionMatrix(types, custom_interactions)
    
    assert matrix.get_interaction(("A", "B")) == 0.5
    assert matrix.get_interaction(("B", "A")) == 0.5  # Spiegelung prüfen
    assert matrix.get_interaction(("B", "C")) == -0.3
    assert matrix.get_interaction(("C", "B")) == -0.3  # Spiegelung prüfen
    assert -1 <= matrix.get_interaction(("A", "C")) <= 1  # Zufälliger Wert

def test_get_interaction():
    """Testet die Abrufbarkeit von Interaktionsstärken."""
    types = ["X", "Y"]
    custom_interactions = {("X", "Y"): 0.7}
    matrix = InteractionMatrix(types, custom_interactions)
    
    assert matrix.get_interaction(("X", "Y")) == 0.7
    assert matrix.get_interaction(("Y", "X")) == 0.7

def test_invalid_type():
    """Testet, ob eine Exception geworfen wird, wenn ein unbekannter Typ angefragt wird."""
    types = ["A", "B"]
    matrix = InteractionMatrix(types)
    
    with pytest.raises(ValueError):
        matrix.get_interaction(("A", "C"))  # "C" existiert nicht

