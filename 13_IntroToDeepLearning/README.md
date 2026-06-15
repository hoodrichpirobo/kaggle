<div align="center">

# Intro to Deep Learning

**Course 13 of 17 - building neural networks with TensorFlow/Keras, from a single dense neuron to regularized classifiers.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Intro%20to%20Deep%20Learning-20BEFF.svg)](https://www.kaggle.com/learn/intro-to-deep-learning)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-3%20of%206-yellow.svg)

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
| 2 | Deep Neural Networks | Complete | [DeepNeuralNetworksExercise.py](./DeepNeuralNetworksExercise.py) |
| 3 | Stochastic Gradient Descent | Complete | [StochasticGradientDescentExercise.py](./StochasticGradientDescentExercise.py) |
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

From the solved exercises so far:

- Defining a neural-network input shape from a tabular training matrix
- Computing the number of input features as `red_wine.shape[1] - 1`
- Building a Keras `Sequential` model
- Adding a single `layers.Dense(units=1, input_shape=input_shape)` layer
- Understanding that a one-unit dense layer on tabular inputs is a learned weighted sum plus bias
- Reading model parameters through `model.weights`
- Separating the learned weight vector from the bias scalar with `w, b = model.weights`
- Deriving a second tabular model input width from the concrete dataset with `concrete.shape[1] - 1`
- Expanding from a single dense neuron to a multilayer network with three 512-unit hidden layers
- Using `relu` activations in hidden layers so stacked dense layers can learn nonlinear relationships
- Keeping the final regression output as `layers.Dense(units=1)` with no activation
- Rewriting inline activations as explicit `layers.Activation("relu")` layers
- Treating activation layers as callable transformations on tensors
- Plotting `relu`, `elu`, `selu`, and `swish` over a fixed input range to compare activation behavior
- Compiling a Keras model for regression with `model.compile(optimizer="adam", loss="mae")`
- Connecting the optimizer, loss function, batch size, and epochs to the actual training loop
- Training with `model.fit(X, y, epochs=200, batch_size=128)` and storing the returned `history`
- Reading learning curves to decide when training has mostly leveled off
- Experimenting with stochastic-gradient-descent behavior by varying learning rate, batch size, and sample count
- Comparing small, medium, and very large batch sizes in the SGD animation
- Recognizing that very large learning rates can prevent convergence entirely
- Treating smaller or medium-sized update steps as a practical default before reaching for extreme settings
- Preserving Kaggle answer checks alongside the solved notebook cells

Expected next skills as the remaining lessons are completed:

- Training with validation data and using validation curves to diagnose generalization
- Reading learning curves for underfitting, overfitting, and convergence behavior across train/validation splits
- Applying early stopping, dropout, and batch normalization
- Designing binary classifiers with sigmoid outputs and cross-entropy loss

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [ASingleNeuronExercise.py](./ASingleNeuronExercise.py) - first Keras model: tabular input shape, one dense output neuron, and direct inspection of weights and bias
  - [DeepNeuralNetworksExercise.py](./DeepNeuralNetworksExercise.py) - multilayer dense regression network with ReLU hidden layers, explicit activation-layer rewrite, and activation-function plots
  - [StochasticGradientDescentExercise.py](./StochasticGradientDescentExercise.py) - compiling with Adam/MAE, fitting over mini-batches and epochs, and experimenting with learning-rate and batch-size behavior
- Completion certificate: pending course completion

## Course Notes

- The first exercise uses Kaggle's provided `red_wine` DataFrame and derives the neural-network input width from every feature column except the target.
- `input_shape = [red_wine.shape[1] - 1]` keeps the model tied to the dataset width instead of hard-coding the feature count.
- The model is intentionally minimal: `keras.Sequential([layers.Dense(units=1, input_shape=input_shape)])`.
- With one dense unit and no activation, the network is equivalent to a linear model. That makes it a clean starting point for understanding how neural networks store coefficients.
- `model.weights` exposes the two learned parameter groups: the feature weights and the bias.
- The deep-network exercise moves to the concrete dataset and again derives `input_shape` from the feature matrix width instead of hard-coding the number of inputs.
- The main regression model stacks three hidden `Dense(512, activation="relu")` layers before a one-unit output layer, making the hidden layers responsible for learned nonlinear representations and the output layer responsible for the final numeric prediction.
- The activation rewrite shows that `activation="relu"` inside a `Dense` layer can also be expressed as a separate `layers.Activation("relu")` layer after the dense transformation.
- The activation comparison plots `relu`, `elu`, `selu`, and `swish` on values from `-3.0` to `3.0`, making the shape of each nonlinear transformation visible before using it inside a model.
- The stochastic-gradient-descent exercise is the first point where model architecture becomes a trained model: `compile` chooses the optimizer and loss, while `fit` runs repeated weight updates over mini-batches.
- The solved regression setup uses the Adam optimizer with mean absolute error, then trains for 200 epochs with batches of 128 examples.
- The returned `history` object is the record to inspect after training; in the saved answer, the learning curves had mostly leveled off.
- The SGD animation experiments isolate three knobs: learning rate, batch size, and number of training examples. The saved trials include very small batches, medium batches, and an intentionally extreme learning rate / batch-size combination.
- The practical lesson from those trials is that smaller batches can help optimization move through the loss surface, while an overly large learning rate can make training fail instead of merely speeding it up.
- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, TensorFlow/Keras setup, and answer-checking helpers (`q_1.check()`, etc.) inside the notebook environment.

## Notes

This course is the handoff from manually shaped model inputs to learned representations. The important habit to carry forward is training accountability: know the input shape, know what each layer changes, know which loss is being optimized, know how the optimizer updates weights, and read validation behavior before trusting a trained network.

## Certificate of Completion

Pending. Add the certificate image here after all six lessons are complete.

<div align="center">

[Back to Roadmap](../README.md)

</div>
