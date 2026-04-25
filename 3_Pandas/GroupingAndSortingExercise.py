# Your code here
reviews_written = reviews.groupby("taster_twitter_handle").size()

# Check your answer
q1.check()

best_rating_per_price = reviews.groupby("price").points.max()
#best_rating_per_price

# Check your answer
q2.check()

price_extremes = reviews.groupby("variety").price.agg([min, max])
# price_extremes

# Check your answer
q3.check()

sorted_varieties = price_extremes.sort_values(by = ["min", "max"], ascending = False)
sorted_varieties

# Check your answer
q4.check()

reviewer_mean_ratings = reviews.groupby("taster_name").points.mean()
reviewer_mean_ratings

# Check your answer
q5.check()

country_variety_counts = reviews.groupby(["country", "variety"]).size().sort_values(ascending = False)
country_variety_counts

# Check your answer
q6.check()
