loans_filepath = "../input/geospatial-learn-course-data/kiva_loans/kiva_loans/kiva_loans.shp"

# Your code here: Load the data
world_loans = gpd.read_file(loans_filepath)

# Check your answer
q_1.check()

# Uncomment to view the first five rows of the data
world_loans.head()

# Your code here
# world.plot()
# world_loans.plot()

ax = world.plot(figsize=(20,20), color='whitesmoke', linestyle=':', edgecolor='black')
world_loans.plot(ax=ax, markersize=2)

# Uncomment to see a hint
q_2.hint()

# Your code here
PHL_loans = world_loans.loc[world_loans.country.isin(["Philippines"])]

# Check your answer
q_3.check()

# Your code here
# ax = world.plot(figsize=(20,20), color='whitesmoke', linestyle=':', edgecolor='black')
# world_loans.plot(ax=ax, markersize=2)

ax = PHL.plot(figsize = (20, 20), color = "whitesmoke", linestyle = ":", edgecolor = "black")
PHL_loans.plot(ax = ax, markersize = 2)

# Uncomment to see a hint
q_4.a.hint()

# View the solution (Run this code cell to receive credit!)
# Sure, on northern mindanao, cagayan valley and a little bit along western visayas and central visayas
q_4.b.solution()


