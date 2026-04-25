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

bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']

# idmax receives a maximum ratio and returns the index, then we pull the title of that row with loc

# Check your answer
q5.check()

def toStars(row):
    if row.points >= 95 or row.country == "Canada":
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
            
star_ratings = reviews.apply(toStars, axis = "columns")

# Check your answer
q7.check()
