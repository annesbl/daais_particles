import pytest
from matrix import InteractionMatrix

def test_interaction_matrix():
    interaction_matrix = InteractionMatrix(["A", "B"], {("A", "B"): 0.5})
    assert interaction_matrix.get_interaction(("A", "B")) == 0.5
