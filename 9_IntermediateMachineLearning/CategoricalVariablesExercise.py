# Fill in the lines below: drop columns in training and validation data
drop_X_train = X_train.select_dtypes(exclude = ["object"])
drop_X_valid = X_valid.select_dtypes(exclude = ["object"])

# Check your answers
step_1.check()

# Check your answer (Run this code cell to receive credit!)
# it's because the training data does not have all the possible values from the categorical variable
step_2.a.check()

from sklearn.preprocessing import OrdinalEncoder

# Drop categorical columns that will not be encoded
label_X_train = X_train.drop(bad_label_cols, axis=1)
label_X_valid = X_valid.drop(bad_label_cols, axis=1)

# Apply ordinal encoder 
ordinal_encoder = OrdinalEncoder()
label_X_train[good_label_cols] = ordinal_encoder.fit_transform(X_train[good_label_cols]) 
label_X_valid[good_label_cols] = ordinal_encoder.transform(X_valid[good_label_cols])
    
# Check your answer
step_2.b.check()

# Fill in the line below: How many categorical variables in the training data
# have cardinality greater than 10?
high_cardinality_numcols = 3

# Fill in the line below: How many columns are needed to one-hot encode the 
# 'Neighborhood' variable in the training data?
num_cols_neighborhood = 25

# Check your answers
step_3.a.check()

# Fill in the line below: How many entries are added to the dataset by 
# replacing the column with a one-hot encoding?
OH_entries_added = 10000 * 99

# Fill in the line below: How many entries are added to the dataset by
# replacing the column with an ordinal encoding?
label_entries_added = 0

# Check your answers
step_3.b.check()

from sklearn.preprocessing import OneHotEncoder

# Use as many lines of code as you need!

OH_encoder = OneHotEncoder(handle_unknown = "ignore", sparse = False)
OH_X_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))     # Your code here
OH_X_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))         # Your code here

OH_X_train.index = X_train.index
OH_X_valid.index = X_valid.index

num_X_train = X_train.drop(object_cols, axis = 1)
num_X_valid = X_valid.drop(object_cols, axis = 1)

OH_X_train = pd.concat([num_X_train, OH_X_train], axis = 1)
OH_X_valid = pd.concat([num_X_valid, OH_X_valid], axis = 1)

OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)

# Check your answer
step_4.check()


