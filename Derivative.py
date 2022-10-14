from sympy.interactive import printing
printing.init_printing(use_latex=True)
import sympy as sp

x = sp.symbols("x")

func = sp.log(x)

derivative = sp.diff(func,x)
print(derivative)