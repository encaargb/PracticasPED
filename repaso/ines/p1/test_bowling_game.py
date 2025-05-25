import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_game_starts_with_zero_score(self):
        game = BowlingGame()
        self.assertEqual(game.score(), 0)

if __name__ == '__main__':
    unittest.main()

def test_roll_zero_keeps_score_zero(self):
    game = BowlingGame()
    game.roll(0)
    self.assertEqual(game.score(), 0)