# Set up the exercise
import math
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex2 import *
print('Setup complete.')

# TODO: Complete the function
def get_expected_cost(beds, baths):
    value = 80000
    value = value + (30000 * beds) + (10000 * baths)
    return value

# Check your answer 
q1.check()

# TODO: Use the get_expected_cost function to fill in each value
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3,2)
option_three = get_expected_cost(3,3)
option_four = get_expected_cost(3,4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)

# Check your answer
q2.check()

# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls + sqft_ceiling) / sqft_per_gallon) * cost_per_gallon
    return cost

# Check your answer
q3.check()


# TODO: Set the project_cost variable to the cost of the project
project_cost = get_cost(432, 144, 400, 15)

# Check your answer
q4.check()

test_value = 2.17

rounded_value = math.ceil(test_value)
print(rounded_value)

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = math.ceil((sqft_walls + sqft_ceiling) / sqft_per_gallon)
    cost = cost * cost_per_gallon
    return cost

# Check your answer
q5.check()

get_actual_cost(432, 144, 400, 15)

get_actual_cost(594, 288, 400, 15)
