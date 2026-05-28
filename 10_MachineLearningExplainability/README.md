<div align="center">

# Machine Learning Explainability

**Course 10 of 17 - interpreting trained models with feature importance, feature effects, and local attribution.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Machine%20Learning%20Explainability-20BEFF.svg)](https://www.kaggle.com/learn/machine-learning-explainability)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-2%20of%205-yellow.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 10 of 17 |
| Estimated time | 4 hours |
| Status | In progress |
| Started | May 28, 2026 |
| Completed | In progress |
| Course page | [Kaggle Learn: Machine Learning Explainability](https://www.kaggle.com/learn/machine-learning-explainability) |

## What This Course Adds

[Intermediate Machine Learning](../9_IntermediateMachineLearning/) made the modeling workflow more reliable: preprocessing lives in pipelines, validation is disciplined, and leakage is treated as a first-class risk. This course adds the next layer: explaining what a fitted model learned and deciding whether those patterns make sense.

The goal is not to decorate a model with charts after the fact. The goal is to use explainability as a debugging and decision tool: identify which features matter, understand how feature values move predictions, inspect individual predictions, and catch suspicious behavior before trusting a score or deploying a workflow.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Use Cases for Model Insights | Complete | Tutorial |
| 2 | Permutation Importance | Complete | [PermutationImportanceExercise.py](./PermutationImportanceExercise.py) |
| 3 | Partial Plots | Not started | Pending |
| 4 | SHAP Values | Not started | Pending |
| 5 | Advanced Uses of SHAP Values | Not started | Pending |

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

## Artifacts

- Exercise solution exported as a Python file for quick review:
  - [PermutationImportanceExercise.py](./PermutationImportanceExercise.py)
- Completion certificate will be added here after the course is finished.

## Course Notes

- The permutation-importance exercise uses a taxi-fare model and asks which location features the model relies on most.
- The first pass fits `PermutationImportance(first_model, random_state=1)` on `val_X` and `val_y`, then displays feature weights with `eli5.show_weights`.
- The exercise then adds `abs_lon_change` and `abs_lat_change` so the model can use a clearer proxy for trip distance instead of relying only on raw pickup and dropoff coordinates.
- A second `RandomForestRegressor(n_estimators=30, random_state=1)` is trained on the engineered feature set before permutation importance is recalculated.
- The written answers preserve the key interpretation: longitude and latitude may matter differently because city geography, route structure, tolls, and vertical versus horizontal travel patterns can affect fare.
- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, and answer-checking helpers inside the notebook environment.

## Notes

This course is the handoff from model building to model interrogation. A strong validation score says a model predicts well on the data it was tested against; explainability asks whether the reasons behind those predictions are understandable, stable, and useful enough to trust.

## Certificate of Completion

Certificate pending until all lessons are complete.

<div align="center">

[Back to Roadmap](../README.md)

</div>
