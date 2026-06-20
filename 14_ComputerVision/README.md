<div align="center">

# Computer Vision

**Course 14 of 17 — teaching neural networks to see with convolution, transfer learning, and image augmentation.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Computer%20Vision-20BEFF.svg)](https://www.kaggle.com/learn/computer-vision)
![Status](https://img.shields.io/badge/Status-In%20Progress-F5A623.svg)
![Lessons](https://img.shields.io/badge/Lessons-1%20of%206-F5A623.svg)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00.svg?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/guide/keras)

`IMAGE → FEATURES → EVIDENCE → CLASS`

[Course Snapshot](#course-snapshot) · [Mental Model](#the-core-mental-model) · [Lessons](#lesson-tracker) · [Implemented Model](#implemented-model) · [Playbook](#computer-vision-playbook) · [Reference](#cnn-shape-reference) · [Artifact](#artifact-guide)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 14 of 17 |
| Estimated time | 4 hours |
| Status | **In progress — 1 of 6 lessons complete** |
| Started | June 20, 2026 |
| Latest completed lesson | The Convolutional Classifier |
| Framework | TensorFlow / Keras |
| Task introduced | Binary image classification with transfer learning |
| Running dataset | Cars versus trucks |
| Course page | [Kaggle Learn: Computer Vision](https://www.kaggle.com/learn/computer-vision) |
| Prerequisite | [Intro to Deep Learning](../13_IntroToDeepLearning/) |

> **Repository truth:** this directory currently contains one completed exercise. The model and conclusions below are implemented; later topics are explicitly marked as the course roadmap.

## What This Course Adds

[Intro to Deep Learning](../13_IntroToDeepLearning/) learned from rows of already prepared features. Computer Vision moves feature engineering *inside* the network. Instead of manually describing an image with edges, textures, shapes, and parts, a convolutional base learns a hierarchy of visual features directly from pixels.

The first exercise makes that shift without discarding the earlier Keras foundation. It reuses a pretrained feature extractor, freezes its learned weights, and attaches a small dense binary-classification head. The result separates the problem into two clean responsibilities:

- **Base:** convert an image into useful feature maps.
- **Head:** convert those learned features into a class probability.

That base/head split is the organizing idea for the entire course.

## The Core Mental Model

```text
RGB image
  [height × width × 3]
          │
          ▼
┌──────────────────────────────┐
│ Pretrained convolutional base│  edges → textures → parts → objects
│          frozen              │  reusable visual feature extractor
└──────────────────────────────┘
          │ feature maps [h × w × channels]
          ▼
      Flatten()
          │ feature vector
          ▼
   Dense(6, ReLU)
          │ learned task-specific evidence
          ▼
 Dense(1, Sigmoid)
          │
          ▼
 P(class = truck) ∈ [0, 1]
```

The important distinction is not “convolutional layers versus dense layers.” It is **representation versus decision**. The base learns what visual evidence looks like; the head learns how that evidence maps to the labels in this dataset.

## Lesson Tracker

| # | Lesson | Status | Evidence |
|:-:|--------|:------:|----------|
| 1 | The Convolutional Classifier | **Complete** | [TheConvolutionalClassifierExercise.py](./TheConvolutionalClassifierExercise.py) |
| 2 | Convolution and ReLU | Not started | — |
| 3 | Maximum Pooling | Not started | — |
| 4 | The Sliding Window | Not started | — |
| 5 | Custom ConvNets | Not started | — |
| 6 | Data Augmentation | Not started | — |

### Course trajectory

```text
Transfer learning
      ↓
Convolution + ReLU
      ↓
Pooling and spatial compression
      ↓
Sliding-window feature extraction
      ↓
Custom convolutional blocks
      ↓
Data augmentation and generalization
```

## Implemented Model

The completed exercise builds a transfer-learning classifier in four decisions.

### 1. Preserve the pretrained representation

```python
pretrained_base.trainable = False
```

Freezing the base prevents large early updates from the randomly initialized head from overwriting useful visual features. Training can therefore focus on the new classification task while retaining the base's existing representation.

### 2. Attach a task-specific head

```python
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    pretrained_base,
    layers.Flatten(),
    layers.Dense(units=6, activation="relu"),
    layers.Dense(units=1, activation="sigmoid"),
])
```

### 3. Match the objective to binary classification

```python
optimizer = tf.keras.optimizers.Adam(epsilon=0.01)

model.compile(
    optimizer=optimizer,
    loss="binary_crossentropy",
    metrics=["binary_accuracy"],
)
```

### 4. Judge the model with validation behavior

The saved exercise reflection reaches a nuanced diagnosis:

- Training and validation loss stay closer together than in the comparison model, indicating **less overfitting**.
- The model converges at a higher loss, indicating **some underfitting**.
- More task-specific capacity is therefore a reasonable next experiment, but only if validation loss improves.

That is the correct way to read learning curves: a smaller train/validation gap is useful, but it does not automatically mean the model is better. **Generalization gap and absolute validation performance are separate questions.**

## Why Each Choice Matters

| Choice | Role | If it is wrong |
|--------|------|----------------|
| Freeze the base | Protect pretrained visual features during initial head training | Early gradients can damage the reusable representation |
| `Flatten()` | Convert spatial feature maps into the vector expected by dense layers | The head receives an incompatible tensor rank |
| Hidden ReLU layer | Learn a nonlinear combination of extracted features | A purely linear head may lack task-specific capacity |
| One sigmoid output | Emit one probability for a binary target | Output shape and label meaning no longer align |
| Binary cross-entropy | Penalize incorrect binary probabilities smoothly | Optimization no longer matches the probabilistic task |
| Binary accuracy | Report thresholded classification performance | A regression metric would be hard to interpret |
| Validation curves | Estimate behavior on unseen images | Training performance can hide memorization |

## Transfer Learning, Precisely

Transfer learning is not just “use a large model.” It is a staged optimization strategy:

1. Start with a base trained on a broad image dataset.
2. Replace its original classifier with a head for the new labels.
3. Freeze the base and train the new head first.
4. Establish a validation baseline.
5. Only then consider unfreezing a small number of late base layers.
6. Fine-tune with a much smaller learning rate and stop when validation performance stops improving.

The exercise implements steps 1–4. Fine-tuning is a possible later experiment, not part of the saved solution.

### Why freezing comes first

At initialization, the new dense head is random. If every layer is trainable immediately, noisy gradients from that head flow through the entire base. A frozen base turns the initial problem into a much safer one: learn a small classifier over stable, already useful features.

### What the model actually learns

With `pretrained_base.trainable = False`:

- the base performs inference and its weights stay fixed;
- the dense head is trainable;
- backpropagation updates only the head;
- the model adapts by learning which existing features distinguish cars from trucks.

## How to Read the Learning Curves

Use loss for model selection and accuracy for human-readable context.

| Curve pattern | Diagnosis | Next move |
|---------------|-----------|-----------|
| Training and validation loss both high and still falling | Training has not converged | Train longer |
| Both losses flatten at a high value | Underfitting | Add head capacity, improve inputs, or carefully fine-tune |
| Training loss falls while validation loss rises | Overfitting | Stop earlier, augment data, regularize, or reduce capacity |
| Both losses flatten low with a small gap | Good fit | Preserve the baseline and evaluate on untouched data |
| Accuracy looks stable but validation loss rises | Predictions are becoming overconfident | Select by validation loss, not accuracy alone |

Never diagnose from the final epoch alone. The *direction and separation* of the curves carry the information.

## Computer Vision Playbook

This is the workflow the course is building toward. Only the transfer-learning stage is implemented so far.

1. **Define the prediction contract.** Decide the label meaning, output shape, and metric before choosing the final layer.
2. **Audit the images.** Inspect class balance, duplicates, corrupt files, resolution, aspect ratio, and label quality.
3. **Split by source, not just by file.** Near-duplicate frames or images from the same subject must not cross train/validation boundaries.
4. **Build the input pipeline.** Decode, resize, batch, normalize exactly as the chosen base expects, then prefetch.
5. **Establish a frozen-base baseline.** Train a small head over pretrained features.
6. **Read validation curves.** Decide whether the real problem is optimization, underfitting, or overfitting.
7. **Add only label-preserving augmentation.** Transformations must preserve the class in the problem's real domain.
8. **Tune capacity deliberately.** Compare head width, pooling strategy, regularization, and learning rate one change at a time.
9. **Fine-tune cautiously.** Unfreeze late layers only after the head is stable; use a low learning rate.
10. **Perform error analysis.** Review false positives and false negatives by class, subgroup, image quality, and confidence.
11. **Lock the test set.** Use it once for the final unbiased estimate, never as a tuning signal.
12. **Record the experiment.** Save the split, seed, preprocessing, architecture, metric, and best checkpoint.

## CNN Shape Reference

Image models are easier to debug when every tensor shape has a meaning.

| Operation | Typical shape change | Learns parameters? | Purpose |
|-----------|----------------------|:------------------:|---------|
| Input batch | `(B, H, W, C)` | No | `B` images, usually `C=3` color channels |
| `Conv2D(F, K)` | `(B, H′, W′, F)` | Yes | Detect `F` learned local patterns with `K×K` kernels |
| `ReLU` | unchanged | No | Keep positive evidence and add nonlinearity |
| `MaxPool2D(P)` | smaller `H`, `W` | No | Compress spatial dimensions and retain strong activations |
| `Flatten` | `(B, H·W·C)` | No | Preserve every activation in one vector |
| `GlobalAveragePooling2D` | `(B, C)` | No | Summarize each feature map with far fewer head parameters |
| `Dense(U)` | `(B, U)` | Yes | Combine extracted evidence for the task |
| `Dense(1, sigmoid)` | `(B, 1)` | Yes | Return a binary class probability |

For a 2D convolution, one useful output-size check is:

```text
output = floor((input + 2 × padding − kernel) / stride) + 1
```

Shape checks catch architectural mistakes early; parameter counts catch unexpectedly expensive heads.

## Concepts Ahead

These topics belong to the remaining five lessons and are not yet claimed as completed work.

### Convolution and ReLU

A convolutional kernel slides across an image and computes the same local pattern detector at every position. ReLU then discards negative responses, leaving a feature map that highlights where the learned pattern appears.

### Maximum pooling

Pooling summarizes small neighborhoods, reduces spatial size, and makes later features less sensitive to small translations. It trades precise location for a more compact representation.

### The sliding window

Weight sharing is why convolution is efficient: one detector is reused across the whole image instead of learning separate weights for every location.

### Custom ConvNets

Reusable convolution → activation → pooling blocks build a feature hierarchy. Earlier blocks respond to simple local patterns; later blocks combine them into task-specific structures.

### Data augmentation

Augmentation creates varied training views without changing the underlying label. It is useful only when each transformation is plausible for the real prediction domain and is applied to training data—not validation or test data.

## Skills Demonstrated

Evidence from the completed exercise:

- Separating a convolutional classifier into a feature-extraction base and classification head
- Reusing a pretrained convolutional representation for a new binary task
- Freezing the base with `pretrained_base.trainable = False`
- Building a Keras `Sequential` transfer-learning model
- Flattening spatial feature maps before a dense head
- Adding task-specific capacity with `Dense(6, activation="relu")`
- Producing a binary probability with `Dense(1, activation="sigmoid")`
- Compiling with Adam, binary cross-entropy, and binary accuracy
- Matching output activation, loss, and metric to the target format
- Comparing training and validation loss as separate signals
- Distinguishing reduced overfitting from unresolved underfitting
- Proposing more capacity from validation evidence rather than training accuracy alone
- Preserving Kaggle's answer checks and written model diagnosis with the solution

## Common Failure Modes

| Symptom | Likely cause | Check first |
|---------|--------------|-------------|
| Validation accuracy is suspiciously high | Duplicate or related images leaked across splits | Group images by source before splitting |
| Loss will not decrease | Wrong labels, output/loss mismatch, or preprocessing mismatch | Inspect one batch and confirm ranges, shapes, and class mapping |
| Training is good; validation degrades | Overfitting | Augmentation validity, head size, early stopping |
| Model predicts one class | Imbalance, reversed labels, or threshold issues | Class counts, inferred class order, confusion matrix |
| Fine-tuning destroys performance | Too many layers unfrozen or learning rate too high | Restore frozen baseline; unfreeze fewer late layers |
| GPU is underused | Input pipeline is the bottleneck | Batching, caching policy, and prefetching |
| Results change unexpectedly | Split or randomness is not controlled | Seeds, deterministic settings, and saved split indices |

## Artifact Guide

### Completed exercise

[TheConvolutionalClassifierExercise.py](./TheConvolutionalClassifierExercise.py) contains the solved Kaggle cells for:

- freezing the supplied pretrained base;
- attaching a `Flatten → Dense(6, ReLU) → Dense(1, Sigmoid)` head;
- compiling the model for binary classification;
- recording the learning-curve diagnosis.

### Execution context

The exported file is **study evidence, not a standalone training script**. Kaggle supplies objects and infrastructure that are intentionally absent from the export, including:

- `pretrained_base`;
- `tf` and the prepared image datasets;
- training/history cells surrounding the exercise prompts;
- `q_1` through `q_4` from Kaggle's answer-checking system.

To reproduce the exercise, open [the course on Kaggle](https://www.kaggle.com/learn/computer-vision), run the lesson notebook in order, and use the exported file as the solved-cell reference.

## Completion Standard

This course will be marked complete only when all six exercise exports and the certificate are present.

- [x] The Convolutional Classifier
- [ ] Convolution and ReLU
- [ ] Maximum Pooling
- [ ] The Sliding Window
- [ ] Custom ConvNets
- [ ] Data Augmentation
- [ ] Completion certificate archived
- [ ] Root roadmap updated from 13/17 to 14/17

## Takeaway

The first lesson's durable idea is architectural separation: **a vision classifier is a learned feature extractor plus a decision head**. Transfer learning works because a representation learned from many images can already encode useful visual structure; the new task often needs only a small classifier to reinterpret that structure.

The engineering discipline is equally important: freeze before fine-tuning, align the output with the loss, trust validation behavior over training performance, and never mistake “less overfit” for “fully fit.”

---

<div align="center">

[← Intro to Deep Learning](../13_IntroToDeepLearning/) · [Back to Roadmap](../README.md) · [Continue on Kaggle →](https://www.kaggle.com/learn/computer-vision)

</div>
