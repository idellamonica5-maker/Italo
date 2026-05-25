import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    var = sympy.Symbol(variabile)
    espressione = sympy.sympify(espressione)
    derivata = sympy.diff(espressione, var)
    return derivata
    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    espressione = sympy.sympify(espressione)
    variabile = sympy.sympify(variabile)
    estremo_inf = sympy.sympify(estremo_inf)
    estremo_sup = sympy.sympify(estremo_sup)
    calcolo_integrale = sympy.integrate(espressione,(variabile, estremo_inf, estremo_sup))
    return calcolo_integrale
    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    espressione = sympy.sympify(espressione)
    variabile = sympy.sympify(variabile)
    punto = sympy.sympify(punto)
    calcolo_limite = sympy.limit(espressione,variabile,punto)
    return calcolo_limite
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:

    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    eq1=sympy.sympify(eq1)
    eq2=sympy.sympify(eq2)
    var1=sympy.sympify(var1)
    var2=sympy.sympify(var2)
    risolvi_sistema_lineare = sympy.solve([eq1, eq2], (var1, var2))
    return risolvi_sistema_lineare
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 +2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x", "x", 0, 1))
    print("Sub-task 3:", calcola_limite("(x**2 - 1)/(x-1)", "x", "1"))
    print("Sub-task 4:", calcola_polinomio_taylor("cos(x)", "x", 0.0, 3))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
