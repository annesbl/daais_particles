import unittest
from Board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(100, 100)

    def test_initialization(self):
        self.assertEqual(self.board.width, 100)
        self.assertEqual(self.board.height, 100)