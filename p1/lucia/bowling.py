class BowlingGame:
    def score(self, rolls): #rolls es una lista porque puede variar el número de tiros al haber bonus
        # Sumamos todos los tiros, sin considerar strikes ni spares (aún)
        return sum(rolls)
