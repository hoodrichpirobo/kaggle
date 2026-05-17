candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
min_mae = float('inf')
max_leaf = -1
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
for each in candidate_max_leaf_nodes:
    current_mae = get_mae(each, train_X, val_X, train_y, val_y)
    if(current_mae <= min_mae):
        max_leaf = each
        min_mae = current_mae

# this is my cp solution.
# the data scientist approach would be storing it in a dictionary and 
# then using the min_mae as key to extract the value in best_tree_size

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = max_leaf
print(best_tree_size)

# Check your answer
step_1.check()

# Fill in argument to make optimal size and uncomment
# final_model = DecisionTreeRegressor(____)
final_model = DecisionTreeRegressor(max_leaf_nodes = best_tree_size, random_state = 1)

# fit the final model and uncomment the next two lines
# final_model.fit(____, ____)
final_model.fit(X, y)

# Check your answer
step_2.check()

# but now we won't have anything to validate with :'(
