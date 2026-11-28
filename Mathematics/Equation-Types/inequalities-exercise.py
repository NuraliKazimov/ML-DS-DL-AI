# inequalities_exercises.py

""" Inequality Exercises """

"""
    1. Simple Inequality with a Loop
       Find all integer x in [a, b] such that 2x – 5 > 3.

    Exercise:
    Write a function `filter_simple(a, b)` that returns a list of all x in the inclusive range [a, b]
    satisfying 2*x - 5 > 3, then print the result for a = -5, b = 10.
"""
# Your Solution...
def filter_simple(a,b):
    result=[]
    for x in range(a,b+1):
        if x**2-4*x+3>0:
            result.append(x)
    return result

print("1) 2x - 5 > 3 for x in [-5,10]:", filter_simple(-5, 10), "\n")



"""
    2. Symbolic Solution with Sympy
       Solve the quadratic inequality x² – 4x + 3 ≤ 0 symbolically.

    Exercise:
    Use sympy’s `solve_univariate_inequality` to find the solution set of
        x**2 - 4*x + 3 <= 0
    and print it.
"""
# Your Solution...

import sympy as sp

x=sp.symbols('x',real=True)
sol=sp.solve_univariate_inequality(x**2-4*x+3<=0,x)

print(sol,"\n")



"""
    3. System of Linear Inequalities with Sympy
       Find the overlap region for:
           x + 2y ≤ 6
           2x -  y ≥ 1

    Exercise:
    Use sympy’s `reduce_inequalities` (or equivalent) to solve the system
        [x + 2*y <= 6,  2*x - y >= 1]
    and display the solution conditions.
"""
# Your Solution...
x, y=sp.symbols('x y')
inequality1= x+ 2*y <6
inequality2= 2*x - y >=1

solution=sp.reduce_inequalities([inequality1,inequality2], x)
solution1=sp.reduce_inequalities([inequality1,inequality2], y)
print(solution)
print(solution1, "\n")


"""
    4. Graphing a Feasible Region with Matplotlib
       Plot the region defined by:
           y ≥ x - 1
           y ≤ -2*x + 4

    Exercise:
    Create a grid over x,y in [-1, 5] and use numpy + matplotlib to shade the intersection
    of the two half-planes. Draw the boundary lines and show the feasible region.
"""
# Your Solution...
import numpy as np
import matplotlib.pyplot as plt

x_vals=np.linspace(-1,5,400)
y_vals=np.linspace(-1,5,400)
x,y=np.meshgrid(x_vals, y_vals)

region1=(y>=x-1)
region2 = (y <= -2*x + 4)


feasible = region1 & region2


plt.figure(figsize=(6,6))
plt.contourf(x, y, feasible, levels=[-0.5, 0.5, 1.5], alpha=0.4)


plt.plot(x_vals,      x_vals - 1,  'b-', label='y = x - 1')
plt.plot(x_vals, -2*x_vals + 4,     'r-', label='y = -2x + 4')


plt.title("Feasible Region: { y ≥ x−1  ∧  y ≤ −2x+4 }")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
plt.show()


"""
    5. Using a List Comprehension
       Filter values in [-5,5] satisfying |x| < 3

    Exercise:
    Write a single list comprehension that produces all integers x between -5 and 5
    for which abs(x) < 3, then print the resulting list.
"""
# Your Solution...
filtered=[x for x in range(-5,6) if abs(x)<3]
print(filtered)
