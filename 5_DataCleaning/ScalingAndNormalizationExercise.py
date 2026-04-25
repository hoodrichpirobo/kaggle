# select the usd_goal_real column
original_goal_data = pd.DataFrame(kickstarters_2017.goal)
original_goal_data

# TODO: Your code here
scaled_goal_data = minmax_scaling(original_goal_data, columns = ["goal"])

# Check your answer
q1.check()

# TODO: Your code here!
index_of_positive_pledged = kickstarters_2017.pledged > 0
positive_pledged = kickstarters_2017.pledged.loc[index_of_positive_pledged]
normalized_pledged = pd.Series(stats.boxcox(positive_pledged)[0],
                              name = "pledged", index = positive_pledged.index)

print("Original data\nPreview:\n", positive_pledged.head())
print("Minimum value:", float(positive_pledged.min()), 
        "\nMaximum value:", float(positive_pledged.max()))
print("-"*30)

print("\nNormalized data\nPreview:\n", normalized_pledged.head())
print("Minimum value:", float(normalized_pledged.min()),
        "\nMaximum value:", float(positive_pledged.max()))

ax = sns.histplot(normalized_pledged, kde = True)
ax.set_title("Normalized data")


