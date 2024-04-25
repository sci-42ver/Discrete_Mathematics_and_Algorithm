# https://stackoverflow.com/a/76443392/21294350
from sympy import symbols, Eq, solve, I
import math
m,n,p,q = symbols('m n p q', complex=True)
eq=(m+n*math.sqrt(5)*I)*(p+q*math.sqrt(5)*I)
eq=eq.expand(complex=True).as_real_imag()
ans = solve(eq)
print(ans) # too slow because the range of these 4 variables is not given