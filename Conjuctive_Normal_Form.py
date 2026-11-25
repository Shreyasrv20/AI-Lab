from sympy import symbols
from sympy.logic.boolalg import (
    Implies, to_cnf
)

P, Q, R = symbols('P Q R')
formula = Implies(P, Q) & Implies(Q, R)

print("Original Expression:", formula)
cnf = to_cnf(formula, simplify=True)

print("CNF Expression:", cnf)