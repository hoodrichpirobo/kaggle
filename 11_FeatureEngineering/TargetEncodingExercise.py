# View the solution (Run this cell to receive credit!)
# I would identify Neighborhood
q_1.check()

# YOUR CODE HERE: Create the MEstimateEncoder
# Choose a set of features to encode and a value for m
encoder = MEstimateEncoder(cols = ["Neighborhood", "SaleType", "MSSubClass", "Exterior1st", "Exterior2nd"], m = 5)

# Fit the encoder on the encoding split
encoder.fit(X_encode, y_encode)

# Encode the training split
X_train = encoder.transform(X_pretrain, y_train)


# Check your answer
q_2.check()

feature = encoder.cols

plt.figure(dpi=90)
ax = sns.distplot(y_train, kde=True, hist=False)
ax = sns.distplot(X_train[feature], color='r', ax=ax, hist=True, kde=False, norm_hist=True)
ax.set_xlabel("SalePrice");
ax.legend(labels=['Encoded Features', 'SalePrice']);

# View the solution (Run this cell to receive credit!)
# The mean-encoded is an exact copy of the target since it doesn't have any duplicates. 
# It worked because it's trained on the exact same data. You should use separate data sets for training encoder and training the model
q_3.check()


