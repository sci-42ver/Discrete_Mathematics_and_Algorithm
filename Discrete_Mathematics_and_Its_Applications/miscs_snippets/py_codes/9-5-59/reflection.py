"""
This is to show the ans
> use the fact that each rotation is the composition of two reflections
"""
# https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html or n-dim https://stackoverflow.com/questions/35681889/multidimensional-symbolic-matrix-in-python#comment59132392_35682521
from sympy import *
init_printing(use_unicode=True)
m,theta,phi,d = symbols('m theta phi d')
m=tan(theta)
P=Matrix([[1, -m], [m, 1]])
P_inv=Inverse(P)
A=Matrix([[1, 0], [0, -1]])
result=simplify(P*A*P_inv)
pprint(result)
# https://en.wikipedia.org/wiki/Rotations_and_reflections_in_two_dimensions#Mathematical_expression
result_2=result.subs(theta,phi)
prod=simplify(result*result_2).subs(2*theta-2*phi,d)
pprint(prod)