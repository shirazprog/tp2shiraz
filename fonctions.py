import math

from expression import Expression
from operations import Multiplication
from polynome import Polynome


class Sin(Expression):
    """Expression representant sin(u)."""

    def __init__(self, expression):
        self.expression = expression

    def evaluer(self, x: float) -> float:
        return math.sin(self.expression.evaluer(x))

    def deriver(self):
        return Multiplication(Cos(self.expression), self.expression.deriver())

    def __str__(self) -> str:
        return f"sin({self.expression})"


class Cos(Expression):
    """Expression representant cos(u)."""

    def __init__(self, expression):
        self.expression = expression

    def evaluer(self, x: float) -> float:
        return math.cos(self.expression.evaluer(x))

    def deriver(self):
        return Multiplication(
            Multiplication(Polynome([-1]), Sin(self.expression)),
            self.expression.deriver()
        )

    def __str__(self) -> str:
        return f"cos({self.expression})"


class Exp(Expression):
    """Expression representant exp(u)."""

    def __init__(self, expression):
        self.expression = expression

    def evaluer(self, x: float) -> float:
        return math.exp(self.expression.evaluer(x))

    def deriver(self):
        return Multiplication(Exp(self.expression), self.expression.deriver())

    def __str__(self) -> str:
        return f"exp({self.expression})"
