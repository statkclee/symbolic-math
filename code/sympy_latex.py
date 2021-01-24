from sympy import *

x, y, z = symbols('x y z')

solveset(Eq(4 * sin(x)**2 -4* cos(pi / 2 +x) -3, 0), x)

solveset(Eq(sin(x), 1/2), x)
4 * sin(x)**2 - 4* cos(pi / 2 +x) -3

from sympy.interactive import printing
printing.init_printing(use_latex = True)

import numpy as np
import sympy as sp

def f(x):
  return np.sin(x)

func = sp.Function('func')

x = sp.Symbol('x')

func = sp.sin(x)

func

inte = sp.Integral(func, x)

inte

answer = sp.integrate(func, x)
answer
