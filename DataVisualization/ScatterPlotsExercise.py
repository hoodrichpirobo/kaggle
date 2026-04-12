# Path of the file to read
candy_filepath = "../input/candy.csv"

# Fill in the line below to read the file into a variable candy_data
candy_data = pd.read_csv(candy_filepath, index_col = "id")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()

# Fill in the line below: Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?  (Please enclose your answer in single quotes.)
more_popular = "3 Musketeers"

# Fill in the line below: Which candy has higher sugar content: 'Air Heads'
# or 'Baby Ruth'? (Please enclose your answer in single quotes.)
more_sugar = "Air Heads"

# Check your answers
step_2.check()

# Scatter plot showing the relationship between 'sugarpercent' and 'winpercent'
sns.scatterplot(x = candy_data.sugarpercent, y = candy_data.winpercent)

# Check your answer
step_3.a.check()

# Candies with more sugar are related with the survey respondents popularity

# Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
sns.regplot(x = candy_data.sugarpercent, y = candy_data.winpercent)

# Check your answer
step_4.a.check()

# Again I think there is a correlation between winpercent and sugarpercent, since there's a positive slope, the sweetness seems to be more popular

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'
sns.scatterplot(x = candy_data.pricepercent, y = candy_data.winpercent, hue = candy_data.chocolate)

# Check your answer
step_5.check()

# Color-coded scatter plot w/ regression lines
sns.lmplot(x = "pricepercent", y = "winpercent", hue = "chocolate", data = candy_data)

# Check your answer
step_6.a.check()

# When it has chocolate, the popularity rises with the more expensive price, whereas the non chocolate candies, they're less popular as the price increases

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'
sns.swarmplot(x = candy_data.chocolate, y = candy_data.winpercent)

# Check your answer
step_7.a.check()

# The plot from step 7 since it's focused on popularity and the chocolate factor without any other variable


