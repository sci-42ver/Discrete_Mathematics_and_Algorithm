# https://www.anthonymorast.com/blog/2021/10/03/taylor-series-in-python/
from TaylorSeries import TaylorSeries
import math
import sympy as sym

def f(x):
    # return math.cos(x) #(math.e**x)*math.sin(x)*math.cos(x)
    return (1+x)/(1-x-x**2) #(math.e**x)*math.sin(x)*math.cos(x)

if __name__ == '__main__':
    pts = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi]
    # pts = [-5, -4, -3, -2, -1, -0.1, 0, 0.1, 1, 2, 3, 4, 5]
    terms = 15
    center = 0
    precision = 3

    ts = TaylorSeries(f, terms, center)
    # ts.print_coefficients()
    # ts.print_equation()

    x = sym.Symbol('x')
    for i in range(1,10):
        # https://scipy-lectures.org/packages/sympy.html#differentiation
        # https://docs.sympy.org/latest/tutorials/intro-tutorial/basic_operations.html
        print(i,(sym.diff(f(x), x, i)/math.factorial(i)).subs(x, 0))
    
    # print("x\tf(x)\tApprox. f(x)\tIntegral f(x)\tDerivative f(x)")
    # for x in pts:
    #     print("{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(x, f(x), ts.approximate_value(x), ts.approximate_integral(0, x), ts.approximate_derivative(x)))
