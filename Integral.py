from code import interact
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import sympy as sp

x = sp.symbols("x")

func = sp.exp(-x**2)

integral = sp.integrate(func,x)
print(integral)