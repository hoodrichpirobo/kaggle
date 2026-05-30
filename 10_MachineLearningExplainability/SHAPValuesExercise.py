# Your code here
import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state = 1).fit(val_X, val_y)
eli5.show_weights(perm, feature_names = val_X.columns.tolist())

from matplotlib import pyplot as plt
from sklearn.inspection import PartialDependenceDisplay

feature_name = "number_inpatient"
PartialDependenceDisplay.from_estimator(my_model, val_X, [feature_name])
plt.show()

# Your Code Here
from matplotlib import pyplot as plt
from sklearn.inspection import PartialDependenceDisplay

feature_name = "time_in_hospital"
PartialDependenceDisplay.from_estimator(my_model, val_X, [feature_name])
plt.show()

#print(pd.Series(data.groupby("time_in_hospital")["readmitted"].mean()))

all_train = pd.concat([train_X, train_y], axis = 1)

all_train.groupby(["time_in_hospital"]).mean().readmitted.plot()
plt.show()

# Your Code Here
import shap

sample_data_for_prediction = val_X.iloc[0].astype(float)

def patient_risk_factors(model, patient_data):

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(patient_data)
    shap.initjs()
    return shap.force_plot(explainer.expected_value[0], shap_values[0], patient_data)


