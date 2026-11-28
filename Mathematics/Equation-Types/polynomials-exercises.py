"""
Polynomial Equations: Exercises

This file contains practice exercises for evaluating, solving, and analyzing polynomial equations.
"""
import cmath
import numpy as np

"""
    1. Evaluate Polynomial
    Exercise:
    Use the evaluate_polynomial function to compute the value of 3x^3 - 2x^2 + x - 5 at x = 2.
    Print the result.
"""
# Your Solution...
def evaluate_poly(coeffs,x):
    result=0
    degree=len(coeffs)-1
    for i, coef in enumerate(coeffs):
        result+= coef*(x**(degree-i))
    return result

print(evaluate_poly([3,-2,1,-5],2), "\n")


"""
    2. Linear Equation
    Exercise:
    Solve the linear equation 5x + 7 = 0 using the solve_linear function.
    Print the solution.
"""
# Your Solution...
def solve_linear(a, b):
    if a == 0:
        raise ValueError("Coefficient a cannot be zero for a linear equation.")
    return [-b / a]

print(solve_linear(5,7), "\n")


"""
    3. Quadratic Formula
    Exercise:
    Solve the equation x^2 - 5x + 6 = 0. Compute the discriminant and both roots using the solve_quadratic function.
    Print the discriminant and roots.
"""
# Your Solution...
def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)
    D = b**2 - 4*a*c
    sqrt_D = cmath.sqrt(D)
    root1 = (-b + sqrt_D) / (2*a)
    root2 = (-b - sqrt_D) / (2*a)

    return [root1, root2]
print(solve_quadratic(1,-5,6), "\n")


"""
    4. Nature of Roots
    Exercise:
    Determine the nature of roots for x^2 + 4x + 5 = 0 using solve_quadratic and discriminant logic.
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...


print(solve_quadratic(1,4,5), "\n")


"""
    5. Cubic Roots
    Exercise:
    Solve the cubic equation x^3 - 6x^2 + 11x - 6 = 0 using the solve_polynomial function.
    Print the roots.
"""
# Your Solution...
def solve_polynomial(cuffs):
    if np is None:
        raise ImportError("NumPy is required for solving general polynomials")
    return np.roots(cuffs)

print(solve_polynomial([1,-6,11,-6]), "\n")

"""
    6. Derivative Polynomial
    Exercise:
    Compute the derivative coefficients of the polynomial 2x^3 - 3x + 5 using the derivative_polynomial function.
    Print the list of derivative coefficients.
"""
# Your Solution...
def derivative_polynomial(cuffs):
    degree = len(cuffs) - 1
    derivatives = [cuffs[i] * (degree - i) for i in range(degree)]
    return derivatives

print(derivative_polynomial([2,-3,5]))
