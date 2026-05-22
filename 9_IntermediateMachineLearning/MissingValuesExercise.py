# Fill in the line below: How many rows are in the training data?
num_rows = 1168

# Fill in the line below: How many columns in the training data
# have missing values?
num_cols_with_missing = 3

# Fill in the line below: How many missing entries are contained in 
# all of the training data?
tot_missing = 212 + 6 + 58

# Check your answers
step_1.a.check()

# Check your answer (Run this code cell to receive credit!)
# I think it would be to use an extension to Imputation
step_1.b.check()

# Fill in the line below: get names of columns with missing values
cols_with_missing = [col for col in X_train.columns
                         if X_train[col].isnull().any()] # Your code here

# Fill in the lines below: drop columns in training and validation data
reduced_X_train = X_train.drop(cols_with_missing, axis = 1)
reduced_X_valid = X_valid.drop(cols_with_missing, axis = 1)

# Check your answers
step_2.check()

from sklearn.impute import SimpleImputer

# Fill in the lines below: imputation
my_imputer = SimpleImputer() # Your code here
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

# Fill in the lines below: imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_valid.columns = X_valid.columns

# Check your answers
step_3.a.check()

# Check your answer (Run this code cell to receive credit!)
# Yeah, i'm very surprised that the imputation was worse than dropping columns, we should then change the imputation method.
step_3.b.check()

# Preprocessed training and validation features
my_imputer = SimpleImputer(strategy = "median")
final_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

final_X_train.columns = X_train.columns
final_X_valid.columns = X_valid.columns

# Check your answers
step_4.a.check()

# Fill in the line below: preprocess test data
final_imputer = SimpleImputer(strategy = "median")
final_X_test = pd.DataFrame(final_imputer.fit_transform(X_test))

# Fill in the line below: get test predictions
preds_test = model.predict(final_X_test)

# Check your answers
step_4.b.check()


