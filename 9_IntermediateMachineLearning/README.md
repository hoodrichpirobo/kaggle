<div align="center">

# Intermediate Machine Learning

**Course 9 of 17 - production-minded tabular modeling with preprocessing, pipelines, validation, XGBoost, and leakage control.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intermediate%20Machine%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intermediate-machine-learning)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-2%20of%207-yellow.svg)

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

## What This Course Adds

[Intro to Machine Learning](../8_IntroToMachineLearning/) established the baseline loop: choose features, split data, train a model, validate with MAE, and submit predictions. This course upgrades that loop for real tabular data, where raw columns are messy, preprocessing must be reproducible, and validation scores are only useful when the workflow avoids leakage.

The focus is not just getting a lower error score. The focus is building a modeling process that can be trusted: transform training and validation data consistently, compare alternatives fairly, keep test data out of fitting steps, and recognize when a model has learned from information it would not have at prediction time.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Introduction | Complete | [IntroductionExercise.py](./IntroductionExercise.py) |
| 2 | Missing Values | Complete | [MissingValuesExercise.py](./MissingValuesExercise.py) |
| 3 | Categorical Variables | Planned | - |
| 4 | Pipelines | Planned | - |
| 5 | Cross-Validation | Planned | - |
| 6 | XGBoost | Planned | - |
| 7 | Data Leakage | Planned | - |

## Modeling Playbook

The course is being used to build a reusable approach for Kaggle-style structured-data problems:

1. Start with a simple validation setup and a known baseline model.
2. Inspect missingness before choosing a preprocessing strategy.
3. Compare dropping columns, imputing values, and preserving missingness signals.
4. Encode categorical variables without leaking information across splits.
5. Move preprocessing into scikit-learn transformers and pipelines.
6. Replace single-split estimates with cross-validation when model selection needs a stronger signal.
7. Use boosted trees when the tabular signal justifies a more powerful model.
8. Audit features for target leakage and train-test contamination before trusting leaderboard gains.

## Core Skills

- Selecting the strongest candidate model from validation performance
- Measuring missingness across rows, columns, and total entries
- Building missing-value column lists with pandas null checks
- Comparing column dropping against numeric imputation
- Applying `SimpleImputer` with consistent fit-on-train, transform-on-valid behavior
- Restoring DataFrame column names after scikit-learn transformations
- Preparing validation and test features with the same preprocessing contract
- Encoding categorical variables for scikit-learn estimators
- Separating numerical and categorical preprocessing paths with `ColumnTransformer`
- Combining preprocessing and modeling into reproducible `Pipeline` objects
- Evaluating model quality with cross-validation instead of one holdout split
- Training boosted tree models with XGBoost for stronger structured-data performance
- Tuning model capacity and learning behavior with validation feedback
- Recognizing target leakage and train-test contamination before they inflate scores

## Artifacts

- Exercise solutions are exported as Python files for quick review:
  - [IntroductionExercise.py](./IntroductionExercise.py)
  - [MissingValuesExercise.py](./MissingValuesExercise.py)
- Future lesson exports will be added here as the course progresses.
- No completion certificate is included yet because the course is still in progress.

## Current Notes

- The introduction exercise records the selected best model and carries it forward as `my_model`.
- The missing-values exercise compares dropping missing columns with imputation, then prepares validation and test features with median imputation.
- The exported `*Exercise.py` files preserve the solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, and answer-checking helpers inside the notebook environment.
- The next README update should move lesson 3 into the completed set once the categorical-variables exercise is exported.

## Notes

This course is the bridge between beginner-friendly model training and a competition-ready tabular workflow. The important shift is discipline: every preprocessing choice has to be evaluated with the same validation rules the model is judged by.

<div align="center">

[Back to Roadmap](../README.md)

</div>
