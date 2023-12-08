from scipy.misc import derivative
import math

class TaylorSeries():
    def __init__(self, function, order, center=0):
        self.center = center
        self.f = function 
        self.order = order
        self.d_pts = order*2
        self.coefficients = []

        # number of points (order) for scipy.misc.derivative
        if self.d_pts % 2 == 0: # must be odd and greater than derivative order
            self.d_pts += 1

        self.__find_coefficients()

    def __find_coefficients(self):
        for i in range(0, self.order+1):
            self.coefficients.append(round(derivative(self.f, self.center, n=i, order=self.d_pts)/math.factorial(i), 5))
            # self.coefficients.append(round(derivative(self.f, self.center, n=i,dx=1e-6)/math.factorial(i), 5))

    def print_equation(self):
        eqn_string = ""
        for i in range(self.order + 1):
            if self.coefficients[i] != 0:
                eqn_string += str(self.coefficients[i]) + ("(x-{})^{}".format(self.center, i) if i > 0 else "") + " + "
        eqn_string = eqn_string[:-3] if eqn_string.endswith(" + ") else eqn_string
        print(eqn_string)

    def print_coefficients(self):
        print(self.coefficients)

    def approximate_value(self, x):
        """
            Approximates the value of f(x) using the taylor polynomial.
            x = point to approximate f(x)
        """
        fx = 0
        for i in range(len(self.coefficients)):
            fx += self.coefficients[i] * ((x - self.center)**i)  # coefficient * nth term 
        return fx

    def approximate_derivative(self, x):
        """
            Estimates the derivative of a function f(x) from its Taylor series.
            Useless since we need the derivative of the actual function to find the series
        """
        value = 0
        for i in range(1, len(self.coefficients)): # skip the first value (constant) as the derivative is 0
            value += self.coefficients[i] * i * ((x - self.center)**(i-1)) # differentiate each term: x^n => n*x^(n-1)
        return value

    def approximate_integral(self, x0, x1):
        """
            Estimates the definite integral of the function using the Taylor series expansion.
            More useful, consider e^x * sin(x), easy to differentiate but difficult to integrate.
            x0 - lower limit of integration
            x1 - upper limit of integration 
        """
        
        # integrals can be off by a constant since int(f(x)) = F(x) + C
        value = 0
        for i in range(len(self.coefficients)):
            value += ((self.coefficients[i] * (1/(i+1)) * ((x1 - self.center)**(i+1))) - 
                      (self.coefficients[i] * (1/(i+1)) * ((x0 - self.center)**(i+1)))) # integrate each term: x^n => (1/n+1)*x^(n+1)
        return value

    def get_coefficients(self):
        """
            Returns the coefficients of the taylor series 
        """
        return self.coefficients
