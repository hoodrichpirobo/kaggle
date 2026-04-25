from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex4 import *
print('Setup complete.')

# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    grade = "A"
    if(score < 60):
        grade = "F"
    elif(score < 70):
        grade = "D"
    elif(score < 80):
        grade = "C"
    elif(score < 90):
        grade = "B"
    return grade
    
# Check your answer
q1.check()

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100
        cost = cost + (len(engraving) * 10)
    else:
        cost = 50
        cost = cost + (len(engraving) * 7)
    return cost

# Check your answer
q2.check()

# TODO: Edit the function to return the correct bill for different
# values of num_gallons
def get_water_bill(num_gallons):
    bill = 1000
    if(num_gallons >= 30001):
        bill = (num_gallons/bill)*10
    elif(num_gallons >= 22001):
        bill = (num_gallons/bill)*7
    elif(num_gallons >= 8001):
        bill = (num_gallons/bill)*6
    elif(num_gallons >= 0):
        bill = (num_gallons/bill)*5
    return bill

# Check your answer
q3.check()

# TODO: Edit the function to return the correct bill for different
# values of GB
def get_phone_bill(gb):
    bill = 100
    if(gb > 15):
        bill = bill + ((gb - 15) * 100)
    return bill

# Check your answer
q4.check()


