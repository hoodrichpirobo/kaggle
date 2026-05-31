# set following variable to 'diag_1_428' or 'payer_code_?'
feature_with_bigger_range_of_effects = "diag_1_428"

# Check your answer
q_1.check()

# Check your answer (Run this code cell to receive credit!)
# Actually no, since changing it could have a lower effect on outcome on a wider range, It could have a relation to higher permutation
# importance if their effect on outcome was big

# Permutation importance
q_2.solution()

# Set following var to "diag_1_428" if changing it to 1 has bigger effect.  Else set it to 'payer_code_?'
bigger_effect_when_changed = "diag_1_428"

# Check your answer
q_3.check()

# Check your answer (Run this code cell to receive credit!)
# That means that all values have a common amount of effect on predictions, whether they are high values or low values
# It could also mean that the variable has an interaction effect with other variables.
q_4.solution()

# Check your answer (Run this code cell to receive credit!)
# Yeah, there's a clear interaction.
# It depends, when feature_of_interest has a lower value, the impact on prediction is proportional to the other_feature,
# but in the case of higher values for feature_of_interest, the impact on prediction is inversely proportional to the other_feature
q_5.solution()

# Your code here
shap.dependence_plot("num_medications", shap_values[1], small_val_X)
shap.dependence_plot("num_lab_procedures", shap_values[1], small_val_X)


