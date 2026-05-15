# print the list of columns in the dataset to find the name of the prediction target
home_data.columns

y = home_data.SalePrice

# Check your answer
step_1.check()

# Create the list of features below
feature_names = ['LotArea',
'YearBuilt',
'1stFlrSF',
'2ndFlrSF',
'FullBath',
'BedroomAbvGr',
'TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Check your answer
step_2.check()

# Review data
# print description or statistics from X
#print(_)
print(X.describe())

print('---------------------------------------------------------------------')
# print the top few lines
#print(_)
print(X.head())

# from _ import _
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model

from sklearn.tree import DecisionTreeRegressor

iowa_model = DecisionTreeRegressor(random_state = 1)

# Fit the model
iowa_model.fit(X, y)

# Check your answer
step_3.check()

predictions = iowa_model.predict(X)
print(predictions)

# Check your answer
step_4.check()

# You can write code in this cell
home_data.SalePrice.head()
home_data.SalePrice.tail()

# all the data I'm seeing is accurate, so i guess that must be because it has been trained with the entire dataset and with many features
# i mean, i understand that as much data used in training, the better the model is, then, right?
