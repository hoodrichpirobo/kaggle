<div align="center">

# Intermediate Machine Learning

**Course 9 of 17 - stronger tabular modeling with preprocessing, validation, XGBoost, and leakage control.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intermediate%20Machine%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intermediate-machine-learning)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-1%20of%207-yellow.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 9 of 17 |
| Estimated time | 4 hours |
| Status | In progress |
| Started | May 20, 2026 |
| Completed | Not yet |
| Course page | [Kaggle Learn: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) |

## Lesson Tracker

| # | Lesson | Exercise |
|:-:|--------|:--------:|
| 1 | Introduction | [Done](./IntroductionExercise.py) |
| 2 | Missing Values | Planned |
| 3 | Categorical Variables | Planned |
| 4 | Pipelines | Planned |
| 5 | Cross-Validation | Planned |
| 6 | XGBoost | Planned |
| 7 | Data Leakage | Planned |

## Core Skills

- Reviewing the baseline supervised-learning workflow from the previous course
- Choosing the best model from validation performance
- Preparing real-world tabular data with missing values
- Comparing column-dropping, imputation, and imputation-with-indicator strategies
- Encoding categorical variables for scikit-learn models
- Separating numerical and categorical preprocessing paths with `ColumnTransformer`
- Combining preprocessing and modeling into reproducible `Pipeline` objects
- Evaluating model quality with cross-validation instead of a single holdout split
- Training boosted tree models with XGBoost for stronger structured-data performance
- Tuning model capacity and learning behavior with validation feedback
- Recognizing target leakage and train-test contamination before they inflate scores
- Keeping preprocessing fitted only on training data so validation remains honest

## Artifacts

- Exercise solutions are exported as Python files for quick review:
  - [IntroductionExercise.py](./IntroductionExercise.py)
- Future lesson exports will be added here as the course progresses.
- No completion certificate is included yet because the course is still in progress.

## Notes

The `*Exercise.py` files preserve solved cells from Kaggle notebooks. They are study references, not always standalone scripts: Kaggle provides datasets, starter variables, and answer-checking helpers inside the notebook environment.

This course builds directly on [Intro to Machine Learning](../8_IntroToMachineLearning/) by replacing the clean, numeric-only workflow with the preprocessing and validation patterns needed for messier real datasets.

<div align="center">

[Back to Roadmap](../README.md)

</div>
