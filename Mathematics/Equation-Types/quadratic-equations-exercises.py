"""
    Quadratic Equations: Exercises
"""

"""
    1. Quadratic Formula
    Exercise:
    Solve the equation x² - 5x + 6 = 0. Compute the discriminant and both roots, then print the results.
"""
# Your Solution...
a,b,c=1,-5,6
D=b**2-4*a*c
D=pow(D,0.5)
x1=(-b+D)/2*a
x2=(-b-D)/2*a
print((x1,x2), "\n")



"""
    2. Nature of Roots
    Exercise:
    Determine the nature of roots for x² + 4x + 5 = 0. 
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
a,b,c=1,4,5
D=b**2-4*a*c
if D>0:
    print("Real and distinct")
elif D==0:
    print("Real and equal")
else:
    print("Complex")

