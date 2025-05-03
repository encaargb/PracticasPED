import unittest                     # Importamos el framework de testing de Python
from bowling import BowlingGame    # Queremos usar la clase que aún no existe (esto provocará el error)

class BowlingGameTest(unittest.TestCase):  # Creamos una clase de test que hereda de unittest.TestCase
    def test_score_all_zeros(self):        # Este es nuestro primer test: partida con 0 bolos
        game = BowlingGame()               # Creamos una partida de bolos
        rolls = [0] * 20                   # Simulamos 20 tiros, todos 0 (una partida entera)
        self.assertEqual(game.score(rolls), 0)  # Esperamos que el resultado sea 0




# Esto permite ejecutar el test si lanzamos este archivo directamente
if __name__ == '__main__':
    unittest.main()
