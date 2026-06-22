<div align="center">

# Computer Vision

**Course 14 of 17 — teaching neural networks to see with convolution, transfer learning, and image augmentation.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Computer%20Vision-20BEFF.svg)](https://www.kaggle.com/learn/computer-vision)
![Status](https://img.shields.io/badge/Status-In%20Progress-F5A623.svg)
![Lessons](https://img.shields.io/badge/Lessons-3%20of%206-F5A623.svg)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00.svg?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/guide/keras)

`IMAGE → FEATURES → EVIDENCE → CLASS`

[Course Snapshot](#course-snapshot) · [Mental Model](#the-core-mental-model) · [Lessons](#lesson-tracker) · [Model](#implemented-model) · [Feature Extraction](#implemented-feature-extraction) · [Playbook](#computer-vision-playbook) · [Reference](#cnn-shape-reference) · [Artifacts](#artifact-guide)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 14 of 17 |
| Estimated time | 4 hours |
| Status | **In progress — 3 of 6 lessons complete** |
| Started | June 20, 2026 |
| Latest completed lesson | Maximum Pooling |
| Framework | TensorFlow / Keras |
| Task introduced | Binary image classification with transfer learning |
| Running dataset | Cars versus trucks |
| Course page | [Kaggle Learn: Computer Vision](https://www.kaggle.com/learn/computer-vision) |
| Prerequisite | [Intro to Deep Learning](../13_IntroToDeepLearning/) |

> **Repository truth:** this directory currently contains three completed exercise exports. Transfer learning, convolution, ReLU, and maximum pooling are backed by saved solutions; the remaining topics are explicitly marked as the course roadmap.

## What This Course Adds

[Intro to Deep Learning](../13_IntroToDeepLearning/) learned from rows of already prepared features. Computer Vision moves feature engineering *inside* the network. Instead of manually describing an image with edges, textures, shapes, and parts, a convolutional base learns a hierarchy of visual features directly from pixels.

The first exercise makes that shift without discarding the earlier Keras foundation. It reuses a pretrained feature extractor, freezes its learned weights, and attaches a small dense binary-classification head. The next two exercises open that feature extractor conceptually: a kernel creates a feature map through convolution, ReLU keeps its positive responses, and maximum pooling condenses nearby activations. Together, the exercises separate the problem into two clean responsibilities:

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
│ Pretrained convolutional base│  convolution → ReLU → pooling
│          frozen              │  reusable visual feature extractor
└──────────────────────────────┘
          │ compact feature maps [h × w × channels]
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

The important distinction is not “convolutional layers versus dense layers.” It is **representation versus decision**. Inside the base, convolution detects local patterns, ReLU shapes their responses, and pooling compresses the spatial evidence. The head then learns how those feature maps correspond to the labels in this dataset.

## Lesson Tracker

| # | Lesson | Status | Evidence |
|:-:|--------|:------:|----------|
| 1 | The Convolutional Classifier | **Complete** | [TheConvolutionalClassifierExercise.py](./TheConvolutionalClassifierExercise.py) |
| 2 | Convolution and ReLU | **Complete** | [ConvolutionAndReLUExercise.py](./ConvolutionAndReLUExercise.py) |
| 3 | Maximum Pooling | **Complete** | [MaximumPoolingExercise.py](./MaximumPoolingExercise.py) |
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

The first exercise builds a transfer-learning classifier in four decisions.

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

## Implemented Feature Extraction

The second and third exercises make the base's core operations concrete:

```text
image patch × kernel → weighted sum → feature-map value → ReLU → local maximum
```

### 1. Define a local feature detector

```python
kernel = tf.constant([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0],
])
```

This sharpening kernel compares each center pixel with its four direct neighbors. Uniform regions change little, while local intensity differences are amplified. The kernel is fixed in this exercise; in a trained convolutional layer, the kernel values are learned from data.

### 2. Apply the kernel across the image

```python
conv_fn = tf.nn.conv2d
```

Convolution reuses the same kernel at every valid location. That **local connectivity** finds small patterns, while **weight sharing** lets one detector recognize its feature anywhere in the image without learning separate weights for every pixel position.

For one input channel and one kernel, each pre-activation is:

```text
feature[i, j] = Σ image_patch[i, j] × kernel
```

Real `Conv2D` layers repeat this operation across input channels and learn many kernels, producing one output feature map per filter.

### 3. Keep positive activations

```python
relu_fn = tf.nn.relu
```

ReLU applies `max(0, x)` elementwise. It clips negative responses to zero, preserves positive matches, and adds the nonlinearity required for stacked convolutional layers to learn more than one linear transformation. The exercise also interprets a supplied directional kernel as a detector for vertical-line features, connecting the arrangement of kernel weights to the pattern highlighted in the output.

### 4. Condense nearby responses

```python
image_condense = tf.nn.pool(
    input=image_detect,
    window_shape=(2, 2),
    pooling_type="MAX",
    strides=(2, 2),
    padding="SAME",
)
```

This operation divides the activated feature map into overlapping or adjacent local windows and keeps the strongest response in each one. With a `2 × 2` window and stride `2`, the spatial dimensions are approximately halved while the channel count is unchanged. `padding="SAME"` retains a final partial window when a dimension is odd, so each output dimension is `ceil(input / 2)`.

Maximum pooling does not learn weights. Its job is to preserve whether a strong local match exists while becoming less sensitive to its exact pixel location. That gives later layers a smaller representation and a modest amount of local translation tolerance, at the deliberate cost of precise spatial detail.

### Local pooling versus global pooling

The exercise also compares local maximum pooling with `GlobalAveragePooling2D` conceptually:

- **Local max pooling** keeps one strong response per neighborhood and preserves a reduced spatial grid.
- **Global average pooling** reduces each complete feature map to one mean value, producing one number per channel.
- **Flattening** keeps every activation and every location, but can create a much larger classification head.

These operations answer different questions. Max pooling asks, “was this feature strong nearby?” Global average pooling asks, “how strongly was this feature present across the image?” Flattening lets the head learn location-specific combinations.

## Why Each Choice Matters

| Choice | Role | If it is wrong |
|--------|------|----------------|
| Kernel shape and weights | Define the local pattern a convolution responds to | The feature map highlights the wrong structure |
| Shared convolution | Apply one detector consistently across spatial positions | Parameter count grows and translation reuse is lost |
| ReLU | Keep positive responses and introduce nonlinearity | Stacked linear operations collapse into one linear mapping |
| `2 × 2` max pooling | Retain strong local responses while reducing height and width | Too much pooling discards useful spatial detail; too little leaves later layers expensive |
| Freeze the base | Protect pretrained visual features during initial head training | Early gradients can damage the reusable representation |
| `Flatten()` | Preserve every spatial activation in one image-level vector | The dense head can become unnecessarily large and location-sensitive |
| Global average pooling | Summarize each channel with one value | Fine spatial layout is intentionally discarded |
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

The first exercise implements steps 1–4. Fine-tuning is a possible later experiment, not part of the saved solution.

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

This is the workflow the course is building toward. The saved work currently implements the transfer-learning baseline and isolates convolution, ReLU, and maximum pooling as feature-extraction steps.

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
| `Flatten` | `(B, H·W·C)` | No | Preserve every activation in one image-level vector |
| `GlobalAveragePooling2D` | `(B, C)` | No | Summarize each feature map with far fewer head parameters |
| `Dense(U)` | `(B, U)` | Yes | Combine extracted evidence for the task |
| `Dense(1, sigmoid)` | `(B, 1)` | Yes | Return a binary class probability |

For a 2D convolution, one useful output-size check is:

```text
output = floor((input + 2 × padding − kernel) / stride) + 1
```

Shape checks catch architectural mistakes early; parameter counts catch unexpectedly expensive heads.

## Concepts Ahead

These topics belong to the remaining three lessons and are not yet claimed as completed work.

### The sliding window

Weight sharing is why convolution is efficient: one detector is reused across the whole image instead of learning separate weights for every location.

### Custom ConvNets

Reusable convolution → activation → pooling blocks build a feature hierarchy. Earlier blocks respond to simple local patterns; later blocks combine them into task-specific structures.

### Data augmentation

Augmentation creates varied training views without changing the underlying label. It is useful only when each transformation is plausible for the real prediction domain and is applied to training data—not validation or test data.

## Skills Demonstrated

Evidence from the three completed exercises:

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
- Defining a `3 × 3` sharpening kernel with `tf.constant`
- Explaining a kernel as a local weighted pattern detector
- Applying convolution with `tf.nn.conv2d`
- Connecting weight sharing to feature detection across spatial positions
- Applying the rectified linear unit with `tf.nn.relu`
- Explaining ReLU as both negative-response clipping and a source of nonlinearity
- Reading the sign and arrangement of kernel weights to identify a directional feature detector
- Applying `2 × 2` maximum pooling with `tf.nn.pool`
- Configuring pooling type, stride, and padding explicitly
- Deriving the spatial output size of stride-2 `SAME` pooling
- Explaining the compression/detail tradeoff introduced by maximum pooling
- Distinguishing local maximum pooling, global average pooling, and flattening
- Preserving Kaggle's answer checks and written model diagnosis with the solution

## Common Failure Modes

| Symptom | Likely cause | Check first |
|---------|--------------|-------------|
| Feature map is empty after ReLU | Kernel responses are negative or preprocessing changed their scale | Inspect values before and after ReLU |
| Feature appears shifted or output size is unexpected | Padding, stride, or kernel dimensions are wrong | Verify the convolution shape formula |
| Small features disappear after pooling | Pooling is too aggressive for the feature-map resolution | Inspect maps before and after pooling; reduce window or stride |
| Validation accuracy is suspiciously high | Duplicate or related images leaked across splits | Group images by source before splitting |
| Loss will not decrease | Wrong labels, output/loss mismatch, or preprocessing mismatch | Inspect one batch and confirm ranges, shapes, and class mapping |
| Training is good; validation degrades | Overfitting | Augmentation validity, head size, early stopping |
| Model predicts one class | Imbalance, reversed labels, or threshold issues | Class counts, inferred class order, confusion matrix |
| Fine-tuning destroys performance | Too many layers unfrozen or learning rate too high | Restore frozen baseline; unfreeze fewer late layers |
| GPU is underused | Input pipeline is the bottleneck | Batching, caching policy, and prefetching |
| Results change unexpectedly | Split or randomness is not controlled | Seeds, deterministic settings, and saved split indices |

## Artifact Guide

### Completed exercises

[TheConvolutionalClassifierExercise.py](./TheConvolutionalClassifierExercise.py) contains the solved Kaggle cells for:

- freezing the supplied pretrained base;
- attaching a `Flatten → Dense(6, ReLU) → Dense(1, Sigmoid)` head;
- compiling the model for binary classification;
- recording the learning-curve diagnosis.

[ConvolutionAndReLUExercise.py](./ConvolutionAndReLUExercise.py) contains the solved Kaggle cells for:

- defining a `3 × 3` sharpening kernel;
- selecting `tf.nn.conv2d` as the convolution operation;
- selecting `tf.nn.relu` as the activation operation;
- interpreting a directional kernel's extracted feature.

[MaximumPoolingExercise.py](./MaximumPoolingExercise.py) contains the solved Kaggle cells for:

- applying `2 × 2` max pooling with stride `2` and `SAME` padding;
- recording the exercise reflections on pooling behavior;
- comparing the role of global average pooling with location-preserving features.

### Execution context

The exported files are **study evidence, not standalone scripts**. Kaggle supplies objects and infrastructure that are intentionally absent from the exports, including:

- `pretrained_base`;
- `tf`, `visiontools`, images, and the prepared image datasets;
- training/history cells surrounding the exercise prompts;
- `q_1` through `q_4` from Kaggle's answer-checking system.

To reproduce an exercise, open [the course on Kaggle](https://www.kaggle.com/learn/computer-vision), run its notebook in order, and use the corresponding export as the solved-cell reference.

## Completion Standard

This course will be marked complete only when all six exercise exports and the certificate are present.

- [x] The Convolutional Classifier
- [x] Convolution and ReLU
- [x] Maximum Pooling
- [ ] The Sliding Window
- [ ] Custom ConvNets
- [ ] Data Augmentation
- [ ] Completion certificate archived
- [ ] Root roadmap updated from 13/17 to 14/17

## Takeaway

The first three lessons establish both levels of the same system: **a vision classifier is a learned feature extractor plus a decision head**, and the extractor is built from local pattern detectors, nonlinear activations, and spatial compression. Transfer learning reuses those already learned detectors; convolution explains how each detector scans an image; ReLU turns its responses into composable evidence; maximum pooling keeps strong local responses while reducing spatial cost.

The engineering discipline is equally important: reason from kernel to feature map, inspect what pooling removes, verify tensor shapes, freeze before fine-tuning, align the output with the loss, trust validation behavior over training performance, and never mistake “less overfit” for “fully fit.”

---

<div align="center">

[← Intro to Deep Learning](../13_IntroToDeepLearning/) · [Back to Roadmap](../README.md) · [Continue on Kaggle →](https://www.kaggle.com/learn/computer-vision)

</div>
