import unittest
from Board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(100, 100)

    def test_initialization(self):
        self.assertEqual(self.board.width, 100)
        self.assertEqual(self.board.height, 100)
        
    def test_get_color_by_type(self):
        color = self.board.get_color_by_type("A")
        self.assertEqual(color, (255, 0, 0))

if __name__ == "__main__":
    unittest.main()