# Check your answer (Run this code cell to receive credit!)
# I would say all latitudes and longitude to calculate the road traveled. Not the passenger_count
q_1.solution()

import eli5
from eli5.sklearn import PermutationImportance

# Make a small change to the code below to use in this problem. 
perm = PermutationImportance(first_model, random_state=1).fit(val_X, val_y)

# Check your answer
q_2.check()

# uncomment the following line to visualize your results
eli5.show_weights(perm, feature_names = val_X.columns.tolist())

# Check your answer (Run this code cell to receive credit!)
# longitudes values were generally closer together and diffferent parts of the city can have different pricing, benefitting longitude. 
# also tolls might be greater travelling vertically than horizontally
q_3.solution()

# create new features
data['abs_lon_change'] = abs(data.dropoff_longitude - data.pickup_longitude)
data['abs_lat_change'] = abs(data.dropoff_latitude - data.pickup_latitude)

features_2  = ['pickup_longitude',
               'pickup_latitude',
               'dropoff_longitude',
               'dropoff_latitude',
               'abs_lat_change',
               'abs_lon_change']

X = data[features_2]
new_train_X, new_val_X, new_train_y, new_val_y = train_test_split(X, y, random_state=1)
second_model = RandomForestRegressor(n_estimators=30, random_state=1).fit(new_train_X, new_train_y)

# Create a PermutationImportance object on second_model and fit it to new_val_X and new_val_y
# Use a random_state of 1 for reproducible results that match the expected solution.
perm2 = PermutationImportance(second_model, random_state = 1).fit(new_val_X, new_val_y)

# show the weights for the permutation importance you just calculated
eli5.show_weights(perm2, feature_names = new_val_X.columns.tolist())

# Check your answer
q_4.check()

# Check your answer (Run this code cell to receive credit!)
# It wouldn't change, because the scale of feature does not affect permutation importance, at least not on a Random Forest
q_5.solution()

# Check your answer (Run this code cell to receive credit!)
# could be, because there can be more toll travelling that way, but we don't have assurance of this
q_6.solution()


