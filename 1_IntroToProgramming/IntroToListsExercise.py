from learntools.core import binder
binder.bind(globals())
from learntools.intro_to_programming.ex5 import *
print('Setup complete.')

# Do not change: Initial menu for your restaurant
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# TODO: remove 'bean soup', and add 'roasted beet salad' to the end of the menu
menu.remove('bean soup')
menu.append('roasted beet salad')

# Do not change: Check your answer
q1.check()

# Do not change: Number of customers each day for the last month
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = (sum(num_customers[:7])/ 7) 
avg_last_seven = (sum(num_customers[-7:])/7) 
max_month = max(num_customers)
min_month = min(num_customers)

# Do not change: Check your answer
q2.check()

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split('.')
formatted_address = address.split(',')

# Do not change: Check your answer
q3.check()


def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked)/len(ratings)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

# Do not change: Check your answer
q4.check()

# TODO: Edit the function
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago - 1])/num_users[len(num_users)- yrs_ago - 1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))

# Do not change: Check your answer
q5.check()
