# Your code here
renamed = reviews.rename(columns = {"region_1" : "region", "region_2" : "locale"})

# Check your answer
q1.check()

reindexed = reviews.rename_axis("wines", axis = "rows")

# Check your answer
q2.check()

combined_products = pd.concat([gaming_products, movie_products])

# Check your answer
q3.check()

# powerlifting_combined = powerlifting_meets.set_index("MeetID")
# powerlifting_combined = powerlifting_competitors.set_index("MeetID")
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
# powerlifting_combined

# Check your answer
q4.check()
