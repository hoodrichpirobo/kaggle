<div align="center">

# Intermediate Machine Learning

**Course 9 of 17 - production-minded tabular modeling with preprocessing, pipelines, validation, XGBoost, and leakage control.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intermediate%20Machine%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intermediate-machine-learning)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-7%20of%207-brightgreen.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 9 of 17 |
| Estimated time | 4 hours |
| Status | Complete |
| Started | May 20, 2026 |
| Completed | May 27, 2026 |
| Course page | [Kaggle Learn: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) |

## What This Course Adds

[Intro to Machine Learning](../8_IntroToMachineLearning/) established the baseline loop: choose features, split data, train a model, validate with MAE, and submit predictions. This course upgrades that loop for real tabular data, where raw columns are messy, preprocessing must be reproducible, and validation scores are only useful when the workflow avoids leakage.

The focus is not just getting a lower error score. The focus is building a modeling process that can be trusted: transform training and validation data consistently, compare alternatives fairly, keep test data out of fitting steps, and recognize when a model has learned from information it would not have at prediction time.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Introduction | Complete | [IntroductionExercise.py](./IntroductionExercise.py) |
| 2 | Missing Values | Complete | [MissingValuesExercise.py](./MissingValuesExercise.py) |
| 3 | Categorical Variables | Complete | [CategoricalVariablesExercise.py](./CategoricalVariablesExercise.py) |
| 4 | Pipelines | Complete | [PipelinesExercise.py](./PipelinesExercise.py) |
| 5 | Cross-Validation | Complete | [CrossValidationExercise.py](./CrossValidationExercise.py) |
| 6 | XGBoost | Complete | [XGBoostExercise.py](./XGBoostExercise.py) |
| 7 | Data Leakage | Complete | [DataLeakageExercise.py](./DataLeakageExercise.py) |

## Modeling Playbook

The course delivered a reusable approach for Kaggle-style structured-data problems:

1. Start with a simple validation setup and a known baseline model.
2. Inspect missingness before choosing a preprocessing strategy.
3. Compare dropping columns, imputing values, and preserving missingness signals.
4. Encode categorical variables without leaking information across splits.
5. Move preprocessing into scikit-learn transformers and pipelines.
6. Replace single-split estimates with cross-validation when model selection needs a stronger signal.
7. Use boosted trees when the tabular signal justifies a more powerful model.
8. Audit features for target leakage and train-test contamination before trusting leaderboard gains.

## Skills Practiced

- Selecting the strongest candidate model from validation performance
- Measuring missingness across rows, columns, and total entries
- Building missing-value column lists with pandas null checks
- Comparing column dropping against numeric imputation
- Applying `SimpleImputer` with consistent fit-on-train, transform-on-valid behavior
- Restoring DataFrame column names after scikit-learn transformations
- Preparing validation and test features with the same preprocessing contract
- Separating numeric-only baselines from categorical-feature experiments
- Identifying categorical columns that are safe for ordinal encoding across train and validation data
- Encoding categorical variables for scikit-learn estimators
- Comparing ordinal encoding with one-hot encoding for low-cardinality features
- Using `OneHotEncoder(handle_unknown="ignore")` to protect validation transforms from unseen categories
- Preserving row indexes and string column names after one-hot encoding
- Separating numerical and categorical preprocessing paths with `ColumnTransformer`
- Combining preprocessing and modeling into reproducible `Pipeline` objects
- Replacing a single validation split with `cross_val_score` for a more stable model-quality estimate
- Scoring a full preprocessing-and-model pipeline across multiple folds without leaking validation data into fitted preprocessing steps
- Comparing `RandomForestRegressor` tree counts by average cross-validated `MAE`
- Selecting `n_estimators=200` from a structured cross-validation sweep
- Training boosted tree models with `XGBRegressor`
- Comparing default XGBoost performance against tuned boosting parameters
- Using a validation set as an `eval_set` for early stopping
- Coordinating `n_estimators`, `learning_rate`, `early_stopping_rounds`, and `n_jobs` for stronger tabular-model experiments
- Recognizing how overly aggressive boosting settings can degrade validation `MAE`
- Distinguishing target leakage from train-test contamination
- Auditing candidate features against the moment a prediction would actually be made in production
- Spotting features that are only available after the target value is known
- Recognizing features that are continuously refit using information that includes the test set
- Selecting the leakage-prone feature from a list of plausible candidates

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [IntroductionExercise.py](./IntroductionExercise.py)
  - [MissingValuesExercise.py](./MissingValuesExercise.py)
  - [CategoricalVariablesExercise.py](./CategoricalVariablesExercise.py)
  - [PipelinesExercise.py](./PipelinesExercise.py)
  - [CrossValidationExercise.py](./CrossValidationExercise.py)
  - [XGBoostExercise.py](./XGBoostExercise.py)
  - [DataLeakageExercise.py](./DataLeakageExercise.py)
- Completion certificate is attached at the bottom of this page.

## Course Notes

- The introduction exercise records the selected best model and carries it forward as `my_model`.
- The missing-values exercise compares dropping missing columns with imputation, then prepares validation and test features with median imputation.
- The categorical-variables exercise compares dropping object columns, ordinal encoding safe categorical columns, and one-hot encoding low-cardinality categorical columns.
- The pipelines exercise wraps numerical imputation, categorical imputation plus one-hot encoding, and a `RandomForestRegressor` inside one reusable scikit-learn pipeline.
- The pipeline now owns the train, validation, and test preprocessing path, which keeps feature transformations consistent when scoring validation data and generating test predictions.
- The cross-validation exercise turns that pipeline into a reusable scoring function, evaluates eight forest sizes from 50 to 400 trees, and selects 200 trees from the average 3-fold `MAE`.
- The XGBoost exercise introduces `XGBRegressor`, compares default boosted trees against a tuned configuration, and uses early stopping on the validation set to avoid wasting boosting rounds.
- The deliberately weak XGBoost configuration with high learning rate and too few trees is preserved as a reminder that model power still needs disciplined validation.
- The data-leakage exercise walks through five business scenarios and forces an explicit decision about whether each candidate feature is safe, would only exist after the target, or is being continuously refit on data that includes the test set.
- The exported `*Exercise.py` files preserve the solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, and answer-checking helpers inside the notebook environment.

## Notes

This course is the bridge between beginner-friendly model training and a competition-ready tabular workflow. The important shift is discipline: every preprocessing choice has to be evaluated with the same validation rules the model is judged by, and every feature has to be auditable against the moment a prediction would actually be made.

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Intermediate%20Machine%20Learning.png"><img src="./Cux%20Prada%20-%20Intermediate%20Machine%20Learning.png" width="600" alt="Intermediate Machine Learning certificate" /></a>

*Completed May 27, 2026.*

</div>

<div align="center">

[Back to Roadmap](../README.md)

</div>
