from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluer(self, x: float) -> float:
        resultat = 0
        for i, coefficient in enumerate(self.coefficients):
            resultat += coefficient * (x ** i)
        return resultat

    def deriver(self) -> "Polynome":
        if len(self.coefficients) <= 1:
            return Polynome([0])

        derives = [i * self.coefficients[i] for i in range(1, len(self.coefficients))]
        return Polynome(derives)

    def __str__(self) -> str:
        termes = []
        for i, coefficient in enumerate(self.coefficients):
            if coefficient == 0:
                continue

            if i == 0:
                termes.append(str(coefficient))
            elif i == 1:
                if coefficient == 1:
                    termes.append("x")
                elif coefficient == -1:
                    termes.append("-x")
                else:
                    termes.append(f"{coefficient}x")
            else:
                if coefficient == 1:
                    termes.append(f"x^{i}")
                elif coefficient == -1:
                    termes.append(f"-x^{i}")
                else:
                    termes.append(f"{coefficient}x^{i}")

        if not termes:
            return "0"

        return " + ".join(termes).replace("+ -", "- ")