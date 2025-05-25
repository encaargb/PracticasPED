import sys
import os
import unittest

# Añadir el directorio src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_game_starts_with_zero_score(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

if __name__ == '__main__':
    unittest.main()
