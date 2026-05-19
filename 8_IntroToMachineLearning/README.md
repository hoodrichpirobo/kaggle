<div align="center">

# Intro to Machine Learning

**Course 8 of 17 - first supervised learning models with pandas and scikit-learn, end to end.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intro%20to%20Machine%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-machine-learning)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-6%20of%206-brightgreen.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 8 of 17 |
| Estimated time | 3 hours |
| Status | Complete |
| Started | May 2026 |
| Completed | May 19, 2026 |
| Course page | [Kaggle Learn: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) |

## Lesson Tracker

| # | Lesson | Exercise |
|:-:|--------|:--------:|
| 1 | How Models Work | Tutorial |
| 2 | Basic Data Exploration | [Done](./BasicDataExplorationExercise.py) |
| 3 | Your First Machine Learning Model | [Done](./YourFirstMachineLearningModelExercise.py) |
| 4 | Model Validation | [Done](./ModelValidationExercise.py) |
| 5 | Underfitting and Overfitting | [Done](./UnderfittingAndOverfittingExercise.py) |
| 6 | Random Forests | [Done](./RandomForestsExercise.py) |
| 7 | Machine Learning Competitions | [Done](./MachineLearningCompetitionsExercise.py) |

## Supplemental Practice

| Topic | File | Notes |
|-------|------|-------|
| Housing Prices competition - greedy forward feature selection | [HousingPricesCompetitionExercise.py](./HousingPricesCompetitionExercise.py) | Picks up where lesson 7 stops: implements greedy forward selection over the 25 numeric features of the Iowa Housing dataset, retrains a `RandomForestRegressor` on the chosen subset, and writes a Kaggle `submission.csv`. |

## Core Skills

- Loading the Iowa home-price training data with pandas
- Inspecting tabular data with `describe()` and summary statistics
- Identifying useful dataset fields before model building
- Defining the prediction target `y` and feature matrix `X`
- Training a baseline `DecisionTreeRegressor` with scikit-learn
- Generating in-sample predictions from selected home features
- Splitting data into training and validation sets with `train_test_split`
- Evaluating validation predictions with mean absolute error (`MAE`)
- Distinguishing in-sample fit from out-of-sample model performance
- Comparing tree sizes with `max_leaf_nodes` to balance underfitting and overfitting
- Selecting a final model configuration from validation-set performance
- Training a `RandomForestRegressor` ensemble for stronger validation performance
- Comparing decision-tree and random-forest models with consistent `MAE` scoring
- Refitting the chosen model on the full training set before scoring the test set
- Producing a Kaggle-shaped `submission.csv` from test-set predictions
- Implementing greedy forward feature selection from scratch (supplemental)

## Artifacts

- Exercise solutions are exported as Python files for quick review:
  - [BasicDataExplorationExercise.py](./BasicDataExplorationExercise.py)
  - [YourFirstMachineLearningModelExercise.py](./YourFirstMachineLearningModelExercise.py)
  - [ModelValidationExercise.py](./ModelValidationExercise.py)
  - [UnderfittingAndOverfittingExercise.py](./UnderfittingAndOverfittingExercise.py)
  - [RandomForestsExercise.py](./RandomForestsExercise.py)
  - [MachineLearningCompetitionsExercise.py](./MachineLearningCompetitionsExercise.py)
- Supplemental practice file: [HousingPricesCompetitionExercise.py](./HousingPricesCompetitionExercise.py)
- The course certificate is included below.

<div align="center">

## Certificate of Completion

<img src="./Cux%20Prada%20-%20Intro%20to%20Machine%20Learning.png" width="600" alt="Kaggle Certificate - Intro to Machine Learning" />

*Completed May 19, 2026*

[Back to Roadmap](../README.md)

</div>
