"""
    1. Simple Equation: ax + b = 0

    Exercise:
    Solve the equation 4x - 8 = 12. Write code to compute x and print the result.
"""
# Your Solution...
a,b,c=4,-8,12
x=(c-b)/a
print("For, 4x - 8 = 12, x=", x, "\n")


"""
    2. Symbolic Solution with Sympy
       Use sympy to solve equations symbolically—handy when you don’t want to rearrange by hand.
    
    Exercise:
    Symbolically solve the equation 7x + 5 = 3x + 13. Use sympy and print the solution.
"""
# Your Solution...
from sympy import symbols, Eq, solve

x=symbols('x')
equation=Eq(7*x + 5, 3*x + 13)
sol=solve(equation,x)
print("For, 7x + 5 = 3x + 13, x=", sol, "\n")


"""
    3. Solving a System of Linear Equations with NumPy
       For multiple variables, write in matrix form Ax=b and use numpy.linalg.solve.
    
    Exercise:
       Solve the system:
           3x + 2y = 11
           2x -  y =  1
       Use numpy.linalg.solve and print x and y.
"""
# Your Solution...
import numpy as np
A=np.array([[3,2],[2,-1]])
B=np.array([11,1])
x,y=np.linalg.solve(A,B)
print(f"x = {x}, y = {y}")
