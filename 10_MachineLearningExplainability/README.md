<div align="center">

# Machine Learning Explainability

**Course 10 of 17 - interpreting trained models with feature importance, partial dependence, and local attribution.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Machine%20Learning%20Explainability-20BEFF.svg)](https://www.kaggle.com/learn/machine-learning-explainability)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-5%20of%205-brightgreen.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 10 of 17 |
| Estimated time | 4 hours |
| Status | Complete |
| Started | May 28, 2026 |
| Completed | May 31, 2026 |
| Course page | [Kaggle Learn: Machine Learning Explainability](https://www.kaggle.com/learn/machine-learning-explainability) |

## What This Course Adds

[Intermediate Machine Learning](../9_IntermediateMachineLearning/) made the modeling workflow more reliable: preprocessing lives in pipelines, validation is disciplined, and leakage is treated as a first-class risk. This course adds the next layer: explaining what a fitted model learned and deciding whether those patterns make sense.

The goal is not to decorate a model with charts after the fact. The goal is to use explainability as a debugging and decision tool: identify which features matter, understand how feature values move predictions, inspect individual predictions, and catch suspicious behavior before trusting a score or deploying a workflow.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Use Cases for Model Insights | Complete | Tutorial |
| 2 | Permutation Importance | Complete | [PermutationImportanceExercise.py](./PermutationImportanceExercise.py) |
| 3 | Partial Plots | Complete | [PartialPlotsExercise.py](./PartialPlotsExercise.py) |
| 4 | SHAP Values | Complete | [SHAPValuesExercise.py](./SHAPValuesExercise.py) |
| 5 | Advanced Uses of SHAP Values | Complete | [AdvancedUsesOfSHAPValuesExercise.py](./AdvancedUsesOfSHAPValuesExercise.py) |

## Explainability Playbook

The course builds a practical sequence for interrogating trained models:

1. Start with the model question: debug performance, improve features, guide data collection, support human decisions, or build trust.
2. Use permutation importance to rank the features the fitted model depends on most.
3. Compare importance results against domain expectations instead of accepting them blindly.
4. Engineer clearer features when raw columns hide the signal the model is actually using.
5. Use partial dependence plots to study average feature effects across many rows.
6. Use SHAP values to explain how features contribute to a single prediction.
7. Move from one-off explanations to summary and dependence views when checking global behavior.
8. Treat explanations as evidence for investigation, not as proof that the model is correct.

## Skills Practiced

- Framing model explainability around concrete use cases
- Distinguishing global model behavior from local prediction explanations
- Installing and using `eli5` for permutation-importance inspection
- Wrapping a fitted scikit-learn model with `PermutationImportance`
- Fitting permutation importance on validation features and targets
- Displaying importance weights with readable feature names
- Interpreting feature rankings from validation-set performance drops
- Reasoning about why raw longitude and latitude features can dominate taxi-fare predictions
- Creating absolute latitude and longitude change features from pickup and dropoff coordinates
- Training a second `RandomForestRegressor` with engineered location-distance features
- Recomputing permutation importance after feature engineering
- Comparing raw coordinate importance against engineered distance-feature importance
- Recognizing that feature scale does not drive permutation importance for tree models
- Treating surprising importance results as prompts for domain investigation
- Building one-way partial dependence plots with `PartialDependenceDisplay.from_estimator`
- Reading partial dependence as the average change in model predictions as a feature changes
- Creating two-feature partial dependence plots for pickup and dropoff longitude interactions
- Comparing partial dependence before and after adding engineered trip-distance features
- Estimating the practical fare impact of shorter taxi trips from partial dependence plots
- Building synthetic feature-response datasets to verify expected partial dependence shapes
- Recognizing when flat partial dependence can hide interaction effects
- Reusing permutation importance and partial dependence on a patient-readmission model
- Plotting `number_inpatient` and `time_in_hospital` partial dependence for readmission risk
- Checking observed readmission rates with grouped training data before trusting a model explanation
- Creating SHAP explanations with `shap.TreeExplainer`
- Converting a single validation row to float-safe patient data for SHAP visualization
- Returning a `shap.force_plot` from a reusable `patient_risk_factors` helper
- Interpreting local feature contributions against the model's expected value
- Reading SHAP summary plots to compare each feature's range of effects across many patients
- Relating the spread of SHAP values to permutation importance when ranking feature influence
- Reasoning about why a wide effect range and a high importance rank do not always coincide
- Building SHAP dependence plots with `shap.dependence_plot` for `num_medications` and `num_lab_procedures`
- Spotting feature interactions where one feature's SHAP effect bends with the value of another
- Recognizing that a consistent or centered SHAP effect can itself be a signal of an interaction

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [PermutationImportanceExercise.py](./PermutationImportanceExercise.py)
  - [PartialPlotsExercise.py](./PartialPlotsExercise.py)
  - [SHAPValuesExercise.py](./SHAPValuesExercise.py)
  - [AdvancedUsesOfSHAPValuesExercise.py](./AdvancedUsesOfSHAPValuesExercise.py)
- Completion certificate: [Cux Prada - Machine Learning Explainability.png](./Cux%20Prada%20-%20Machine%20Learning%20Explainability.png)

## Course Notes

- The permutation-importance exercise uses a taxi-fare model and asks which location features the model relies on most.
- The first pass fits `PermutationImportance(first_model, random_state=1)` on `val_X` and `val_y`, then displays feature weights with `eli5.show_weights`.
- The exercise then adds `abs_lon_change` and `abs_lat_change` so the model can use a clearer proxy for trip distance instead of relying only on raw pickup and dropoff coordinates.
- A second `RandomForestRegressor(n_estimators=30, random_state=1)` is trained on the engineered feature set before permutation importance is recalculated.
- The written answers preserve the key interpretation: longitude and latitude may matter differently because city geography, route structure, tolls, and vertical versus horizontal travel patterns can affect fare.
- The partial-plots exercise uses `PartialDependenceDisplay.from_estimator` to inspect how the taxi-fare model's predictions move as one coordinate changes.
- Two-dimensional partial dependence is used to compare pickup and dropoff longitude together, making short-trip structure visible in the model response surface.
- After adding `abs_lon_change` and `abs_lat_change`, the repeated pickup-longitude plot checks whether the engineered distance features make the raw coordinate effect less misleading.
- The synthetic-data sections test partial dependence against known formulas, including a piecewise effect and a pure interaction where permutation importance sees signal but one-way partial dependence can look flat.
- The SHAP values exercise moves to a hospital readmission model, first checking global signals with permutation importance and partial dependence before explaining one patient-level prediction.
- `number_inpatient` and `time_in_hospital` are inspected with partial dependence, while grouped observed readmission rates provide a reality check against the model's learned relationship.
- `patient_risk_factors` wraps `shap.TreeExplainer`, `explainer.shap_values`, `shap.initjs`, and `shap.force_plot` so one validation patient can be explained relative to the model baseline.
- The advanced-SHAP exercise stays on the readmission model and moves from single predictions to dataset-wide views: SHAP summary plots compare each feature's range of effects, and the written answers reason about why a wide effect range does not have to line up with the top permutation-importance rank.
- `shap.dependence_plot` is used on `num_medications` and `num_lab_procedures` to expose interaction effects, where a feature's contribution bends depending on the value of another feature rather than staying constant.
- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, and answer-checking helpers inside the notebook environment.

## Notes

This course is the handoff from model building to model interrogation. A strong validation score says a model predicts well on the data it was tested against; explainability asks whether the reasons behind those predictions are understandable, stable, and useful enough to trust.

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Machine%20Learning%20Explainability.png"><img src="./Cux%20Prada%20-%20Machine%20Learning%20Explainability.png" width="600" alt="Machine Learning Explainability certificate" /></a>

*Completed May 31, 2026.*

</div>

<div align="center">

[Back to Roadmap](../README.md)

</div>
