# Import the train_test_split function and uncomment
# from _ import _
from sklearn.model_selection import train_test_split

# fill in and uncomment
# train_X, val_X, train_y, val_y = ____
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Check your answer
step_1.check()

# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state = 1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Check your answer
step_2.check()

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# Check your answer
step_3.check()

# print the top few validation predictions
# print(val_predictions[0:10])
# print the top few actual prices from validation data
# print(val_y[0:10])

pd.DataFrame({
    "prediction": val_predictions[:10],
    "actual" : val_y.iloc[:10].values
})

from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y, val_predictions)

# uncomment following line to see the validation_mae
print(val_mae)

# Check your answer
step_4.check()


