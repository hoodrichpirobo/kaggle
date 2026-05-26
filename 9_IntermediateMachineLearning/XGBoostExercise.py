from xgboost import XGBRegressor

# Define the model
my_model_1 = XGBRegressor(random_state = 0) # Your code here

# Fit the model
my_model_1.fit(X_train, y_train) # Your code here

# Check your answer
step_1.a.check()

from sklearn.metrics import mean_absolute_error

# Get predictions
predictions_1 = my_model_1.predict(X_valid) # Your code here

# Check your answer
step_1.b.check()

# Calculate MAE
mae_1 = mean_absolute_error(predictions_1, y_valid) # Your code here

# Uncomment to print MAE
print("Mean Absolute Error:" , mae_1)

# Check your answer
step_1.c.check()

# Define the model
my_model_2 = XGBRegressor(n_estimators = 1000, learning_rate = 0.05, n_jobs = -1) # Your code here

# Fit the model
my_model_2.fit(X_train, y_train,
              early_stopping_rounds = 5,
              eval_set = [(X_valid, y_valid)],
              verbose = False) # Your code here

# Get predictions
predictions_2 =  my_model_2.predict(X_valid)# Your code here

# Calculate MAE
mae_2 = mean_absolute_error(predictions_2, y_valid) # Your code here

# Uncomment to print MAE
print("Mean Absolute Error:" , mae_2)

# Check your answer
step_2.check()

# Define the model
my_model_3 = XGBRegressor(n_estimators = 50, learning_rate = 1)

# Fit the model
my_model_3.fit(X_train, y_train) # Your code here

# Get predictions
predictions_3 = my_model_3.predict(X_valid)

# Calculate MAE
mae_3 = mean_absolute_error(predictions_3, y_valid)

# Uncomment to print MAE
print("Mean Absolute Error:" , mae_3)

# Check your answer
step_3.check()


