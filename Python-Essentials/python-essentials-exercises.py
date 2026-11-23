"""

    1. Data Types Practice
    
    Exercise:
    Define and print the following variables:

    * An integer (`int`) with a value of 10.
    * A floating-point number (`float`) representing 9.81.
    * A string (`str`) that says "Python Essentials".
    * A list (`list`) containing numbers from 1 to 5.
    * A tuple (`tuple`) with two coordinates: (50, 100).
    * A dictionary (`dict`) with keys `name` (value: "John") and `age` (value: 28).
    * A set (`set`) containing numbers {1, 2, 2, 3}.
    * A boolean (`bool`) variable set to `False`.
"""

# Your Solution...
intNumber=10
floatNumber=9.81
string="Python Essentials"
list=[1,2,3,4,5]
tuple=(50,100)
dictionary={"name":"John", "age":28}
set={1,2,2,3}
boolean=False
print(intNumber, "\n", floatNumber,"\n", string,"\n", list,"\n", tuple,"\n", dictionary,"\n", set, "\n",boolean, "\n")




"""
    2. Iteration Practice
    
    Exercise:
    
    * Use a `for` loop to print numbers from 10 to 1 (descending).
    * Use a `while` loop to print even numbers between 2 and 10.
    * Use a list comprehension to create a list of cubes of numbers from 1 to 5 and print it.
"""

# Your Solution...
for i in range(10,0,-1):
    print(i)
print("\n")
i=2
while i<10:
    if i%2==0:
        print(i)
    i=i+1
print("\n")
myList=[x**3 for x in range(1,6)]
print(myList, "\n")



"""
    3. Functions Practice
    
    Exercise:
    Create the following functions:
    
    * A function named `area_of_circle` that takes radius as input and returns the area of a circle.
    * A function named `is_even` that returns `True` if a number is even, otherwise `False`.
    * A lambda function `multiply` that multiplies two numbers.
    
    Demonstrate each function with sample inputs.
"""

# Your Solution...
def area_of_circle(radius):
    return 3.14*radius*radius

def is_even(num):
    if num%2==0:
        return True
    else:
        return False

var = lambda num1, num2: num1 + num2

print(area_of_circle(5))
print(is_even(17))
print(var(4,5))







"""
    4. Importing and Using Libraries
    
    Exercise:
    
    * Import `math` and use it to calculate and print the square root of 64.
    * Import NumPy with alias `np` and create a NumPy array `[10, 20, 30, 40, 50]`, then print it.
    * Import `randint` from the `random` module and print a random integer between 5 and 15.
"""

# Your Solution...
import math
import numpy as np
from random import randint
arr=np.array([10,20,30,40,50])
print(math.sqrt(64),arr,randint(5,15), "\n")



"""
    5. Symbolic Math with SymPy
    
    Exercise:
    Use SymPy to solve symbolically the quadratic equation: x^2 - 5x + 6 = 0. Print the solutions.
"""

# Your Solution...
import sympy as sp

x=sp.symbols('x')
equation=x**2-5*x+6
result=sp.solve(equation)
print(result, "\n")


"""
    6. Solving Equations with NumPy
    
    Exercise:
    Use NumPy to solve the following system of equations and print the solutions for x and y:
    4x + 3y = 20
    2x - y = 2
"""

# Your Solution...
A=np.array([[4,3],[2,-1]])
B=np.array([20,2])
solution=np.linalg.solve(A,B)
print(solution, "\n")
