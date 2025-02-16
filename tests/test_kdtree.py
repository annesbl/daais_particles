import pytest
import numpy as np
from interaction import KDTree

def test_kdtree_initialization():
    positions = np.array([[0, 0], [1, 1], [2, 2]])
    tree = KDTree.initialise_tree(positions)
    assert tree is not None
