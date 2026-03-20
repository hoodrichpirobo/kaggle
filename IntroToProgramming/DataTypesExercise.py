# Set up the exercise
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex3 import *
print('Setup complete.')

# Define a float
y = 1.
print(y)
print(type(y))

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z))

# Uncomment and run this code to get started!
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

# Check your answer (Run this code cell to receive credit!)
q1.check()

# Uncomment and run this code to get started!
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False))

# Check your answer (Run this code cell to receive credit!)
q2.check()

# TODO: Complete the function
def get_expected_cost(beds, baths, has_basement):
    value = 80000 + (beds * 30000) + (baths * 10000) + (has_basement * 40000)
    return value

# Check your answer 
q3.check()

# Uncomment to see a hint
q3.hint()

# Uncomment to view the solution
q3.solution()

print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

# Check your answer (Run this code cell to receive credit!)
q4.check()

def cost_of_project(engraving, solid_gold):
    cost = (solid_gold * 100)
    cost = cost + ((not solid_gold )* 50)
    cost = cost + (solid_gold * len(engraving) * 10)
    cost = cost + ((not solid_gold) * len(engraving) * 7)
    return cost

# Check your answer
q5.check()


