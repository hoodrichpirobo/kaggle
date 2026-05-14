import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path)

# Call line below with no argument to check that you've loaded the data correctly
step_1.check()

# Print summary statistics in next line
home_data.describe()

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 2026 - 2010

# Checks your answers
step_2.check()

# If explanation 1 is true, then the model is trustworthy, otherwise it isn't. 

# If it is true, then the model cannot know what hasn't happened yet (the creation of new houses)

# If it isn't, then the model is outdated and has to keep up with newer trends.
