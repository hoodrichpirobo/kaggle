# Your code here
desc = reviews.description # this is a Series

# Check your answer
q1.check()

first_description = reviews.description.iloc[0]

# Check your answer
q2.check()
first_description

first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row

first_row = reviews.iloc[0]

# Check your answer
q3.check()
first_row

sample_reviews = reviews.iloc[[1, 2,3,5,8]]

# Check your answer
q5.check()
sample_reviews

sample_reviews = reviews.iloc[[1, 2,3,5,8], :]

# Check your answer
q5.check()
sample_reviews

df = reviews.loc[:99, ['country', 'variety']]

# Check your answer
q7.check()
df

italian_wines = reviews.loc[reviews.country == 'Italy']

# Check your answer
q8.check()

top_oceania_wines = reviews.loc[(reviews.points >= 95) & (reviews.country.isin(['Australia','New Zealand']))]

# Check your answer
q9.check()
top_oceania_wines
