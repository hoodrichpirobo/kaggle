median_points = reviews.points.median()

# Check your answer
q1.check()

countries = reviews.country.unique()

# Check your answer
q2.check()

countries = reviews.country.unique()

# Check your answer
q2.check()

centered_price = reviews.price - reviews.price.mean()

# Check your answer
q4.check()

bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']

# idmax receives a maximum ratio and returns the index, then we pull the title of that row with loc

# Check your answer
q5.check()


