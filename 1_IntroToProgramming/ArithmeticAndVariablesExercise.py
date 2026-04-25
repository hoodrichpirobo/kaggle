# Set up the exercise
from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex1 import *
print('Setup complete.')

print("Hello, world!")

# DO NOT REMOVE: Mark this question as completed
q1.check()

# TODO: Change the message
print("Good morning!")

# DO NOT REMOVE: Mark this question as completed 
q2.check()

# Uncomment to get a hint
q3.hint()

# Uncomment to view solution
q3.solution()

# DO NOT REMOVE: Check your answer
q3.check()

# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

# TODO: Set the value of the births_per_min variable
births_per_min = 250

# TODO: Set the value of the births_per_day variable
births_per_day = mins_per_hour * hours_per_day * births_per_min

# DO NOT REMOVE: Check your answer
q4.check()

# Uncomment to get a hint
#q4.hint()

# Uncomment to view solution
#q4.solution()

# Load the data from the titanic competition
import pandas as pd
titanic_data = pd.read_csv("../input/titanic/train.csv")

# Show the first five rows of the data
titanic_data.head()

# Number of total passengers
total = len(titanic_data)
print(total)

# Number of passengers who survived
survived = (titanic_data.Survived == 1).sum()
print(survived)

# Number of passengers under 18
minors = (titanic_data.Age < 18).sum()
print(minors)

# TODO: Fill in the value of the survived_fraction variable
survived_fraction = survived/total 

# Print the value of the variable
print(survived_fraction)

# TODO: Fill in the value of the minors_fraction variable
minors_fraction = minors/total

# Print the value of the variable
print(minors_fraction)

# DO NOT REMOVE: Check your answer
q5.check()

# Uncomment to receive a hint
#q5.hint()

# Uncomment to view the solution
#q5.solution()
