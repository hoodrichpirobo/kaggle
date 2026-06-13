<div align="center">

# Intro to Deep Learning

**Course 13 of 17 - building neural networks with TensorFlow/Keras, from a single dense neuron to regularized classifiers.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intro%20to%20Deep%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-deep-learning)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-1%20of%206-yellow.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 13 of 17 |
| Estimated time | 4 hours |
| Status | In progress |
| Started | June 13, 2026 |
| Completed | TBD |
| Course page | [Kaggle Learn: Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) |

This course starts the deep-learning section of the track after the repository's classical machine-learning, feature-engineering, explainability, and forecasting work.

## What This Course Adds

[Time Series](../12_TimeSeries/) used carefully engineered features and classical models to learn from ordered data. Intro to Deep Learning changes the modeling unit: instead of manually defining most of the representation, a neural network learns layered transformations from data.

The course begins with the smallest possible Keras model - one dense neuron with a weight for each input feature and one bias term - then expands toward deeper networks, stochastic optimization, regularization, and binary classification. The practical goal is to understand what each architectural and training choice does before moving into larger computer-vision and applied deep-learning work.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | A Single Neuron | Complete | [ASingleNeuronExercise.py](./ASingleNeuronExercise.py) |
| 2 | Deep Neural Networks | Not started | TBD |
| 3 | Stochastic Gradient Descent | Not started | TBD |
| 4 | Overfitting and Underfitting | Not started | TBD |
| 5 | Dropout and Batch Normalization | Not started | TBD |
| 6 | Binary Classification | Not started | TBD |

## Deep Learning Playbook

The course builds a practical sequence for moving from linear models to neural networks:

1. Treat a single neuron as a learned linear function: weighted inputs plus a bias.
2. Use `input_shape` to make the model's expected feature count explicit.
3. Stack dense layers so hidden layers can learn intermediate representations.
4. Add nonlinear activations so the network can model more than straight-line relationships.
5. Train with stochastic gradient descent by iteratively updating weights from batches of examples.
6. Track validation loss to separate real learning from memorization.
7. Use capacity control, early stopping, dropout, and batch normalization to improve generalization.
8. Switch the output layer, loss function, and metrics when the task changes from regression to classification.

## Skills Practiced

From the solved exercise so far:

- Defining a neural-network input shape from a tabular training matrix
- Computing the number of input features as `red_wine.shape[1] - 1`
- Building a Keras `Sequential` model
- Adding a single `layers.Dense(units=1, input_shape=input_shape)` layer
- Understanding that a one-unit dense layer on tabular inputs is a learned weighted sum plus bias
- Reading model parameters through `model.weights`
- Separating the learned weight vector from the bias scalar with `w, b = model.weights`
- Preserving Kaggle answer checks alongside the solved notebook cells

Expected next skills as the remaining lessons are completed:

- Building multilayer dense networks with hidden layers and activation functions
- Compiling Keras models with optimizers, losses, and metrics
- Training models with `fit`, batches, epochs, and validation data
- Reading learning curves for underfitting, overfitting, and convergence behavior
- Applying early stopping, dropout, and batch normalization
- Designing binary classifiers with sigmoid outputs and cross-entropy loss

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [ASingleNeuronExercise.py](./ASingleNeuronExercise.py) - first Keras model: tabular input shape, one dense output neuron, and direct inspection of weights and bias
- Completion certificate: pending course completion

## Course Notes

- The first exercise uses Kaggle's provided `red_wine` DataFrame and derives the neural-network input width from every feature column except the target.
- `input_shape = [red_wine.shape[1] - 1]` keeps the model tied to the dataset width instead of hard-coding the feature count.
- The model is intentionally minimal: `keras.Sequential([layers.Dense(units=1, input_shape=input_shape)])`.
- With one dense unit and no activation, the network is equivalent to a linear model. That makes it a clean starting point for understanding how neural networks store coefficients.
- `model.weights` exposes the two learned parameter groups: the feature weights and the bias.
- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, TensorFlow/Keras setup, and answer-checking helpers (`q_1.check()`, etc.) inside the notebook environment.

## Notes

This course is the handoff from manually shaped model inputs to learned representations. The important habit to carry forward is architectural accountability: know the input shape, know what each layer changes, know which loss is being optimized, and read validation behavior before trusting a trained network.

## Certificate of Completion

Pending. Add the certificate image here after all six lessons are complete.

<div align="center">

[Back to Roadmap](../README.md)

</div>
