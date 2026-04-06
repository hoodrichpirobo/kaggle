# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()

point_strings = reviews.points.astype("str")

# Check your answer
q2.check()

n_missing_prices = reviews.price.isnull().sum()

# Check your answer
q3.check()

reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending = False)
# reviews_per_region

# Check your answer
q4.check()
