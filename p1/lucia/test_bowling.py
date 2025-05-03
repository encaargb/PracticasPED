import unittest                     # Importamos el framework de testing de Python
from bowling import BowlingGame    # Queremos usar la clase que aún no existe (esto provocará el error)

class BowlingGameTest(unittest.TestCase):  # Creamos una clase de test que hereda de unittest.TestCase
    def test_score_all_zeros(self):        # Este es nuestro primer test: partida con 0 bolos
        game = BowlingGame()               # Creamos una partida de bolos
        rolls = [0] * 20                   # Simulamos 20 tiros, todos 0 (una partida entera)
        self.assertEqual(game.score(rolls), 0)  # Esperamos que el resultado sea 0

    def test_score_all_ones(self):
        game = BowlingGame()
        rolls = [1] * 20 # Simulamos 20 tiros, todos 1
        self.assertEqual(game.score(rolls), 20) # Esperamos que el resultado sea 20 (1 por tiro, 20 tiros)

    def test_one_spare(self): # Test de spare
        game = BowlingGame()
        # Simulamos una partida con:
        # Ronda 1: 5 + 5 → spare → bonus = siguiente tiro (3)
        # Ronda 2: 3 + 0
        # Total esperado: 10 + 3 (bonus) + 3 = 16
        rolls = [5, 5, 3] + [0] * 17  # 20 tiros en total
        self.assertEqual(game.score(rolls), 16)
        



# Esto permite ejecutar el test si lanzamos este archivo directamente
if __name__ == '__main__':
    unittest.main()
