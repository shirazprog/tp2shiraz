from expression import Expression


class Addition(Expression):
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def evaluer(self, x: float) -> float:
        return self.gauche.evaluer(x) + self.droite.evaluer(x)

    def deriver(self):
        return Addition(self.gauche.deriver(), self.droite.deriver())

    def __str__(self) -> str:
        return f"({self.gauche} + {self.droite})"


class Multiplication(Expression):
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def evaluer(self, x: float) -> float:
        return self.gauche.evaluer(x) * self.droite.evaluer(x)

    def deriver(self):
        return Addition(
            Multiplication(self.gauche.deriver(), self.droite),
            Multiplication(self.gauche, self.droite.deriver())
        )

    def __str__(self) -> str:
        return f"({self.gauche} * {self.droite})"
