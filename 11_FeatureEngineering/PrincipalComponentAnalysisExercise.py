# View the solution (Run this cell to receive credit!)
# I think for PC1, since all features have the same sign, describes a contrast between houses having large values and houses having small values
# On the other hand, I think PC3 shows a contrast between big GrLivArea and worst TotalBsmtSF
q_1.check()

X = df.copy()
y = X.pop("SalePrice")

X = X.join(X_pca)
score = score_dataset(X, y)
print(f"Your score: {score:.5f} RMSLE")

# Check your answer
q_2.check()

# View the solution (Run this cell to receive credit!)
# It seems like they're coming from Partial Sales on Edwards 
q_3.check()
