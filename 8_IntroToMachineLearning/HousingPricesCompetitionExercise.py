# Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the data, and separate the target
file_path = '/kaggle/input/competitions/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(file_path)
y = home_data.SalePrice

features = ['MSSubClass',
'LotArea',
'OverallQual',
'OverallCond',
'YearBuilt',
'YearRemodAdd',
'1stFlrSF',
'2ndFlrSF',
'LowQualFinSF',
'GrLivArea',
'FullBath',
'HalfBath',
'BedroomAbvGr',
'KitchenAbvGr',
'TotRmsAbvGrd',
'Fireplaces',
'WoodDeckSF',
'OpenPorchSF',
'EnclosedPorch',
'3SsnPorch',
'ScreenPorch',
'PoolArea',
'MiscVal',
'MoSold',
'YrSold']

model = RandomForestRegressor(random_state=1, n_jobs = -1)
X = home_data[features]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


'''
This serves the purpose of iterating through the combination of test features
until I obtain the best combination in an time affordable way, the best approach would
be to iterate all 33.5 million times
'''
def get_mae(selected_features):
    model.fit(train_X[selected_features], train_y)
    preds = model.predict(val_X[selected_features])
    
    return mean_absolute_error(val_y, preds)

# Here's my attempt at implementing by myself a greedy forward selection.

best_mae = float('inf')
selected_features = []
remaining_features = features.copy()

while len(remaining_features):
    best_feature_this_round = None
    best_mae_this_round = float('inf')

    # ROUND STARTS
    
    for feature in remaining_features:
        trial_features = selected_features + [feature]

        current_mae = get_mae(trial_features)
        print(f"Trying {trial_features} -> MAE: {current_mae:,.0f}")

        if current_mae < best_mae_this_round:
            best_mae_this_round = current_mae
            best_feature_this_round = feature

    # ROUND ENDS, CHOOSE WHICH FEATURE TO ADD
    
    if best_mae_this_round < best_mae:
        selected_features.append(best_feature_this_round)
        remaining_features.remove(best_feature_this_round)
        best_mae = best_mae_this_round

        print()
        print(f"Added feature: {best_feature_this_round}")
        print(f"New best MAE: {best_mae:,.0f}")
        print(f"Current selected_features: {selected_features}")
        print("-" * 60)
    else:
        print("No feature improved the MAE, stopping.")
        break

print(f"Final ({len(selected_features)}) selected features):")
print(selected_features)

print()
    
# scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}


print("Validation MAE for Random Forest Model: {:,.0f}".format(best_mae))

# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state = 1, n_jobs = -1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X[selected_features], y)

test_data_path = '/kaggle/input/competitions/home-data-for-ml-course/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)

test_X = test_data[selected_features]

# make predictions which we will submit. 
test_preds = rf_model_on_full_data.predict(test_X)

output = pd.DataFrame({'Id': test_data.Id,
                      'SalePrice': test_preds})
output.to_csv('submission.csv', index = False)
