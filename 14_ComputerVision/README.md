<div align="center">

# Computer Vision

**Course 14 of 17 — teaching neural networks to see with convolution, transfer learning, image augmentation, and accelerator-ready Kaggle workflows.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Computer%20Vision-20BEFF.svg)](https://www.kaggle.com/learn/computer-vision)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-6%20of%206-brightgreen.svg)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00.svg?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/guide/keras)

`IMAGE → FEATURES → EVIDENCE → CLASS`

[Course Snapshot](#course-snapshot) · [Mental Model](#the-core-mental-model) · [Lessons](#lesson-tracker) · [Transfer Model](#implemented-transfer-learning-model) · [Feature Extraction](#implemented-feature-extraction) · [Custom ConvNet](#implemented-custom-convnet) · [Augmentation](#implemented-data-augmentation) · [Supplemental](#supplemental-practice) · [Playbook](#computer-vision-playbook) · [Reference](#cnn-shape-reference) · [Artifacts](#artifact-guide)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 14 of 17 |
| Estimated time | 4 hours |
| Status | **Complete — 6 of 6 lessons** |
| Started | June 20, 2026 |
| Completed | June 25, 2026 |
| Final lesson | Data Augmentation |
| Framework | TensorFlow / Keras |
| Task introduced | Binary image classification with transfer learning, custom ConvNets, and data augmentation |
| Running dataset | Cars versus trucks |
| Supplemental practice | Two multiclass vision submission workflows: flowers with VGG16 and cassava leaf disease with ResNet50, plus one Higgs Boson TPU workflow with a wide-and-deep binary classifier |
| Repository artifacts | 6 lesson exports, 3 supplemental practice workflows, 1 completion certificate |
| Course page | [Kaggle Learn: Computer Vision](https://www.kaggle.com/learn/computer-vision) |
| Prerequisite | [Intro to Deep Learning](../13_IntroToDeepLearning/) |

> **Repository truth:** this directory contains all six official lesson exports, three supplemental practice workflows, and the completion certificate. Transfer learning, convolution, ReLU, maximum pooling, sliding-window extraction, 1D convolutional filtering, custom convolutional blocks, dropout, data augmentation, TPU-aware input pipelines, Kaggle submission formatting, and wide-and-deep binary classification are all backed by saved work.

## What This Course Adds

[Intro to Deep Learning](../13_IntroToDeepLearning/) learned from rows of already prepared features. Computer Vision moves feature engineering *inside* the network. Instead of manually describing an image with edges, textures, shapes, and parts, a convolutional base learns a hierarchy of visual features directly from pixels.

The first exercise makes that shift without discarding the earlier Keras foundation. It reuses a pretrained feature extractor, freezes its learned weights, and attaches a small dense binary-classification head. The next three exercises open that feature extractor conceptually: a kernel creates a feature map through convolution, ReLU keeps its positive responses, maximum pooling condenses nearby activations, and the sliding-window exercise makes stride and padding explicit. The fifth exercise then assembles those operations into a trainable convolutional hierarchy and adds dropout to the classification head. The final exercise introduces label-preserving augmentation and integrates it into a larger batch-normalized ConvNet. Together, the exercises separate the problem into two clean responsibilities:

- **Base:** convert an image into useful feature maps.
- **Head:** convert those learned features into a class probability.

That base/head split is the organizing idea for the entire course.

The supplemental vision submission files apply the same split to larger multiclass settings. The flowers workflow streams image TFRecords, detects whether TPU distribution is available, freezes a VGG16 convolutional base, replaces the classifier with `GlobalAveragePooling2D` plus a softmax head over the flower classes, trains with a learning-rate schedule, and writes predictions in Kaggle submission format. The cassava workflow repeats that production shape for plant-disease labels with explicit train/validation TFRecord splitting, a frozen ResNet50 base, ResNet preprocessing, an exponential learning-rate decay, and ordered test-ID submission output.

The third supplemental file is adjacent accelerator practice rather than an official computer-vision lesson. It uses the Higgs Boson TFRecord dataset to train a TPU-aware wide-and-deep binary classifier over 28 tabular features, keeping the same high-throughput `tf.data`, distribution-strategy, validation-curve, and metric discipline while leaving image-specific convolution behind.

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
| 4 | The Sliding Window | **Complete** | [TheSlidingWindowExercise.py](./TheSlidingWindowExercise.py) |
| 5 | Custom ConvNets | **Complete** | [CustomConvnetsExercise.py](./CustomConvnetsExercise.py) |
| 6 | Data Augmentation | **Complete** | [DataAugmentationExercise.py](./DataAugmentationExercise.py) |

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

## Implemented Transfer-Learning Model

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

### 5. Slide the detector deliberately

The fourth exercise makes the geometry of feature extraction explicit by choosing an image, choosing a kernel, and controlling how the detector moves:

```python
image = car
kernel = emboss

visiontools.show_extraction(
    image,
    kernel,
    conv_stride=1,
    conv_padding="valid",
    pool_size=2,
    pool_stride=2,
    pool_padding="same",
)
```

`conv_stride=1` moves the kernel one pixel at a time, so adjacent feature-map values come from heavily overlapping image patches. `conv_padding="valid"` computes responses only where the whole kernel fits inside the image. Pooling then uses a `2 × 2` window with stride `2`, while `pool_padding="same"` keeps the reduced grid from dropping a final partial pooling window.

The saved answer check records a `7 × 7` convolution output for the selected image/kernel setup. That number is not trivia; it is the visible consequence of input size, kernel size, stride, and padding.

### 6. Reuse the same idea in one dimension

The sliding-window concept is not limited to images. The exercise repeats it over a time series with `tf.nn.conv1d`:

```python
ts_filter = tf.nn.conv1d(
    input=ts_data,
    filters=kern,
    stride=1,
    padding="VALID",
)
```

The `detrend`, `average`, and `spencer` kernels each scan across neighboring time steps and replace every local window with one weighted response. In images, the response becomes a spatial feature map. In a time series, it becomes a filtered signal. The same core operation is doing both jobs: a shared kernel slides across local neighborhoods and exposes a pattern.

## Implemented Custom ConvNet

The fifth exercise replaces the frozen pretrained base with a feature extractor learned entirely from the cars-versus-trucks training data:

```python
model = keras.Sequential([
    layers.Conv2D(32, 3, activation="relu", padding="same",
                  input_shape=[128, 128, 3]),
    layers.MaxPool2D(),

    layers.Conv2D(64, 3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.Conv2D(128, 3, activation="relu", padding="same"),
    layers.Conv2D(128, 3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.Flatten(),
    layers.Dense(6, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(1, activation="sigmoid"),
])
```

The architecture increases channel capacity as spatial resolution falls:

| Stage | Output shape, excluding batch | What changes |
|-------|-------------------------------|--------------|
| Input | `128 × 128 × 3` | RGB image |
| `Conv2D(32, 3, same)` | `128 × 128 × 32` | Learn 32 local feature detectors |
| `MaxPool2D()` | `64 × 64 × 32` | Halve height and width |
| `Conv2D(64, 3, same)` | `64 × 64 × 64` | Expand the feature vocabulary |
| `MaxPool2D()` | `32 × 32 × 64` | Compress spatial evidence again |
| Two `Conv2D(128, 3, same)` layers | `32 × 32 × 128` | Compose deeper features before discarding more location detail |
| `MaxPool2D()` | `16 × 16 × 128` | Produce the final feature maps |
| `Flatten()` | `32,768` | Convert spatial maps into one vector |
| `Dense(6) → Dropout(0.2) → Dense(1)` | `1` | Regularize the head and emit a binary probability |

With these input dimensions, the model has **437,453 trainable parameters**. The `Flatten → Dense(6)` transition alone contributes 196,614, which is why the head remains small and includes dropout even though the convolutional base grows deeper.

```python
model.compile(
    optimizer=tf.keras.optimizers.Adam(epsilon=0.01),
    loss="binary_crossentropy",
    metrics=["binary_accuracy"],
)
```

The output contract is unchanged from the transfer-learning model: one sigmoid probability trained with binary cross-entropy and reported with binary accuracy. The optimization problem is different, however. The transfer model trains only a new head over fixed general-purpose features; this custom model must learn every convolutional filter and the head from the course dataset.

The saved exercise reflection reports that the model still overfits, but performs somewhat better than the tutorial comparison despite adding another convolutional layer. Its explanation attributes the improved control to `Dropout(0.2)`. That is evidence for a useful experiment, not proof that dropout alone caused the improvement; a controlled comparison would keep the architecture, split, initialization, and training schedule fixed while changing only dropout.

## Implemented Data Augmentation

The final exercise treats augmentation as a modeling assumption rather than a generic switch. A transformation is valid only when it changes the pixels without changing the correct label.

The saved exploration applies candidate transformations independently and repeatedly to the same training image. For example:

```python
augment = keras.Sequential([
    preprocessing.RandomContrast(factor=0.5),
])

for i in range(16):
    image = augment(ex, training=True)
```

The same visual check is repeated for horizontal flips, width changes, and translations. Viewing multiple randomized versions makes the decision concrete: horizontal flips and modest geometric changes are plausible for cars and trucks, while vertical flips or aggressive color changes may violate assumptions in other domains. For example, an orientation change that is harmless for a flower classifier could destroy the meaning of an aerial-image label, and a color shift could erase a class-defining flower color.

The final cars-versus-trucks model keeps only conservative transformations:

```python
model = keras.Sequential([
    layers.InputLayer(input_shape=[128, 128, 3]),

    preprocessing.RandomContrast(factor=0.10),
    preprocessing.RandomFlip(mode="horizontal"),
    preprocessing.RandomRotation(factor=0.10),

    layers.BatchNormalization(renorm=True),
    layers.Conv2D(64, 3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.BatchNormalization(renorm=True),
    layers.Conv2D(128, 3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.BatchNormalization(renorm=True),
    layers.Conv2D(256, 3, activation="relu", padding="same"),
    layers.Conv2D(256, 3, activation="relu", padding="same"),
    layers.MaxPool2D(),

    layers.BatchNormalization(renorm=True),
    layers.Flatten(),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid"),
])
```

The augmentation layers run inside the model during training and leave validation or inference inputs unchanged. This keeps preprocessing attached to the saved architecture and avoids contaminating validation data with randomized training views.

The network expands capacity from 64 to 128 to 256 filters while reducing the image from `128 × 128` to `16 × 16`. The final feature maps flatten to 65,536 activations before the eight-unit head; that `Flatten → Dense(8)` transition alone contributes 524,296 parameters and remains the model's largest single parameter block.

The saved reflection reports a small amount of remaining overfitting but a large overall performance improvement over the earlier course models. That supports augmentation plus the larger architecture as the strongest saved configuration, while still stopping short of attributing the gain to any one change without an ablation study.

## Supplemental Practice

Three supplemental workflows extend the course material beyond the six official Kaggle Learn lessons. Two are end-to-end competition-style vision submissions that exercise the same representation/head pattern on larger multiclass image-classification tasks. The third is a non-vision TPU benchmark that reinforces the shared deep-learning infrastructure: TFRecords, accelerator strategy, large batches, regularization, callbacks, and validation metrics.

### Flowers submission workflow

[CreateYourFirstSubmissionExercise.py](./CreateYourFirstSubmissionExercise.py) covers:

- loading Kaggle-hosted image TFRecords through `KaggleDatasets().get_gcs_path`;
- decoding JPEG bytes into normalized `512 × 512 × 3` tensors;
- building `tf.data` train, validation, and test pipelines with parallel reads, batching, caching or prefetching, and unordered reads where order is not semantically required;
- detecting TPU availability and selecting the matching TensorFlow distribution strategy;
- applying label-preserving horizontal-flip augmentation in the input pipeline;
- reusing VGG16 as a frozen ImageNet feature extractor with `include_top=False`;
- replacing the ImageNet head with `GlobalAveragePooling2D` and `Dense(len(CLASSES), activation="softmax")`;
- compiling with Adam, sparse categorical cross-entropy, and sparse categorical accuracy for multiclass labels;
- scheduling the learning rate with a ramp-up and exponential decay;
- converting test predictions and image IDs into a Kaggle-compatible `submission.csv`.

### Cassava leaf-disease workflow

[TPUsPlusCassavaLeafDiseaseExercise.py](./TPUsPlusCassavaLeafDiseaseExercise.py) covers:

- loading competition TFRecords from the active Kaggle dataset context;
- parsing labeled records with `target` labels and unlabeled records with `image_name` IDs;
- splitting train TFRecord shards into training and validation sets with `train_test_split`;
- decoding images to normalized `512 × 512 × 3` tensors for TPU execution;
- applying horizontal-flip augmentation in the input pipeline;
- batching by `16 * strategy.num_replicas_in_sync`;
- preserving unordered reads for training throughput and ordered reads for test IDs;
- using `tf.keras.applications.resnet50.preprocess_input` before a frozen ResNet50 base;
- attaching `GlobalAveragePooling2D`, a small ReLU layer, and a five-class softmax output;
- compiling with Adam, sparse categorical cross-entropy, and sparse categorical accuracy;
- training with an exponential learning-rate decay;
- writing image IDs and predicted disease labels to `submission.csv`.

### Higgs Boson TPU workflow

[DetectingtheHiggsBosonWithTPUsExercise.py](./DetectingtheHiggsBosonWithTPUsExercise.py) covers:

- loading the Kaggle-hosted Higgs Boson TFRecord dataset through `KaggleDatasets().get_gcs_path("higgs-boson")`;
- parsing serialized 28-feature float tensors and binary labels from each record;
- tracking 500,000 validation examples within an 11-million-example dataset;
- detecting TPU availability and scaling batch size by `strategy.num_replicas_in_sync`;
- streaming cached, repeated, shuffled, batched, and prefetched datasets into the training loop;
- building repeated `Dense → BatchNormalization → Activation → Dropout` blocks with 2,048 hidden units;
- combining a linear path and deep network through `keras.experimental.WideDeepModel`;
- compiling with binary cross-entropy, Adam, AUC, binary accuracy, and `experimental_steps_per_execution`;
- using `EarlyStopping` and `ReduceLROnPlateau` to stop or slow training from validation evidence;
- plotting cross-entropy loss and AUC curves after training.

These artifacts are also a useful contrast with the official lessons. The course exercises focus on cars-versus-trucks binary classification and on understanding CNN operations directly. The two vision submission workflows add the surrounding production shape of Kaggle image competitions: scalable input formats, accelerator strategy, multiclass output contracts, ordered test IDs, and submission-file assembly. The Higgs workflow keeps the accelerator and validation discipline but swaps pixels for dense feature tensors, making clear which habits are vision-specific and which generalize to high-throughput deep learning.

## Why Each Choice Matters

| Choice | Role | If it is wrong |
|--------|------|----------------|
| Kernel shape and weights | Define the local pattern a convolution responds to | The feature map highlights the wrong structure |
| Shared convolution | Apply one detector consistently across spatial positions | Parameter count grows and translation reuse is lost |
| ReLU | Keep positive responses and introduce nonlinearity | Stacked linear operations collapse into one linear mapping |
| `2 × 2` max pooling | Retain strong local responses while reducing height and width | Too much pooling discards useful spatial detail; too little leaves later layers expensive |
| Convolution stride | Control how far the detector moves between neighboring responses | Large strides skip local evidence; tiny strides cost more computation |
| Convolution padding | Decide whether border pixels can contribute to the output | Unexpected shape changes or border artifacts appear |
| Pooling stride and padding | Control spatial compression after activation | Useful responses may be dropped or output dimensions may surprise later layers |
| 1D convolution filters | Apply the same sliding-window logic to ordered sequences | The filter detrends, smooths, or emphasizes the wrong time-series behavior |
| Increasing filter counts | Trade spatial resolution for a richer learned feature vocabulary | Too few filters bottleneck the model; too many add cost and overfitting risk |
| `padding="same"` in custom blocks | Preserve height and width until pooling performs deliberate compression | Unplanned shrinking can erase border information and collapse maps too quickly |
| Two convolutions before the third pool | Compose features at the same spatial resolution before downsampling | Pooling too early can remove detail before deeper combinations are learned |
| Freeze the base | Protect pretrained visual features during initial head training | Early gradients can damage the reusable representation |
| `Flatten()` | Preserve every spatial activation in one image-level vector | The dense head can become unnecessarily large and location-sensitive |
| Global average pooling | Summarize each channel with one value | Fine spatial layout is intentionally discarded |
| Hidden ReLU layer | Learn a nonlinear combination of extracted features | A purely linear head may lack task-specific capacity |
| `Dropout(0.2)` | Reduce reliance on individual head activations during training | Too little may not regularize; too much can cause underfitting |
| ResNet preprocessing | Match raw image tensors to the preprocessing expected by a ResNet50 base | The pretrained representation receives inputs on the wrong scale or color convention |
| Label-preserving augmentation | Expose the model to plausible variation without collecting new labels | Invalid transformations teach the model that changed or impossible examples retain the original class |
| In-model augmentation layers | Apply random transforms during training and preserve deterministic evaluation | Augmenting validation data makes model comparison noisy and changes the evaluation distribution |
| Batch normalization with renormalization | Stabilize intermediate activation scales across convolutional stages | Poorly estimated statistics can destabilize training, especially with small batches |
| TFRecord streaming | Feed large image or tabular datasets efficiently to accelerators | Training stalls, memory use grows, or order-sensitive IDs drift |
| Distribution strategy | Keep TPU, GPU, and CPU execution behind one training interface | Batch size, model scope, and callback behavior can stop matching the hardware |
| Wide-and-deep modeling | Combine a linear path with nonlinear feature interactions | The model may miss either simple additive signal or deeper interactions |
| One sigmoid output | Emit one probability for a binary target | Output shape and label meaning no longer align |
| Binary cross-entropy | Penalize incorrect binary probabilities smoothly | Optimization no longer matches the probabilistic task |
| Binary accuracy | Report thresholded classification performance | A regression metric would be hard to interpret |
| AUC | Measure binary ranking quality across thresholds | Accuracy can hide weak discrimination, especially when class balance is uneven |
| Validation curves | Estimate behavior on unseen examples | Training performance can hide memorization |

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

This is the workflow the course builds toward. The saved work implements a frozen-base transfer-learning baseline, a custom ConvNet, and an augmented batch-normalized ConvNet, while also isolating convolution, ReLU, maximum pooling, sliding windows, and 1D filters as feature-extraction steps.

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

## Skills Demonstrated

Evidence from the six completed exercises and supplemental workflows:

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
- Choosing an image/kernel pair for visual feature-extraction inspection
- Configuring convolution stride, convolution padding, pool size, pool stride, and pool padding together
- Reading a `7 × 7` convolution output as a consequence of sliding-window geometry
- Interpreting valid padding as "only positions where the kernel fully fits"
- Reformatting a 1D series into batch/channel dimensions for TensorFlow convolution
- Applying `tf.nn.conv1d` with `VALID` padding to a time-series signal
- Comparing detrending, averaging, and Spencer filters as sliding kernels over ordered data
- Building a custom Keras ConvNet for `128 × 128 × 3` RGB inputs
- Stacking `Conv2D → ReLU → MaxPool2D` stages into a learned feature hierarchy
- Increasing learned filters from 32 to 64 to 128 as spatial dimensions shrink
- Preserving resolution inside convolutional blocks with `padding="same"`
- Stacking two 128-filter convolutions before the final pooling operation
- Tracing the custom model from `128 × 128 × 3` input to `16 × 16 × 128` final feature maps
- Flattening 32,768 learned activations into a six-unit classification head
- Applying `Dropout(0.2)` before the sigmoid output to regularize the head
- Compiling the custom classifier with Adam, binary cross-entropy, and binary accuracy
- Distinguishing a fully trainable custom base from a frozen pretrained base
- Treating the saved dropout explanation as a hypothesis that requires a controlled comparison
- Comparing randomized contrast, horizontal flip, width, and translation transformations visually
- Judging augmentation choices against the label semantics of the target domain
- Rejecting transformations that could alter class meaning rather than applying augmentation indiscriminately
- Embedding `RandomContrast(0.10)`, horizontal `RandomFlip`, and `RandomRotation(0.10)` in a Keras model
- Applying augmentation during training while preserving deterministic validation and inference behavior
- Building a batch-normalized ConvNet with 64-, 128-, and 256-filter stages
- Flattening `16 × 16 × 256` feature maps into an eight-unit binary-classification head
- Reading the final learning curves as improved overall performance with slight residual overfitting
- Treating the combined architecture and augmentation result as evidence that still requires ablation to isolate causes
- Preserving Kaggle's answer checks and written model diagnosis with the solution
- Building `tf.data` pipelines around TFRecord image shards
- Detecting TPU availability and training under the selected distribution strategy
- Freezing VGG16 as a multiclass image feature extractor
- Freezing ResNet50 as a multiclass plant-disease feature extractor
- Applying the application-specific ResNet50 preprocessing layer before the frozen base
- Splitting training TFRecord shards into train and validation subsets with a fixed random state
- Using global average pooling to keep the classifier head compact
- Training a softmax classifier with sparse categorical cross-entropy
- Writing ordered test predictions to `submission.csv`
- Parsing serialized Higgs feature tensors and labels from TFRecords
- Training a TPU-aware wide-and-deep binary classifier over dense tabular features
- Combining `keras.experimental.LinearModel` with a regularized deep network
- Monitoring binary classification with both AUC and binary accuracy
- Controlling large-model training with early stopping and learning-rate reduction callbacks

## Common Failure Modes

| Symptom | Likely cause | Check first |
|---------|--------------|-------------|
| Feature map is empty after ReLU | Kernel responses are negative or preprocessing changed their scale | Inspect values before and after ReLU |
| Feature appears shifted or output size is unexpected | Padding, stride, or kernel dimensions are wrong | Verify the convolution shape formula |
| Small features disappear after pooling | Pooling is too aggressive for the feature-map resolution | Inspect maps before and after pooling; reduce window or stride |
| Validation accuracy is suspiciously high | Duplicate or related images leaked across splits | Group images by source before splitting |
| Loss will not decrease | Wrong labels, output/loss mismatch, or preprocessing mismatch | Inspect one batch and confirm ranges, shapes, and class mapping |
| Training is good; validation degrades | Overfitting | Augmentation validity, head size, early stopping |
| Augmentation hurts validation performance | Transformations are too strong or do not preserve the label | Visualize repeated transformed samples and remove implausible operations |
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

[TheSlidingWindowExercise.py](./TheSlidingWindowExercise.py) contains the solved Kaggle cells for:

- selecting a car image and emboss kernel for extraction visualization;
- configuring convolution and pooling stride/padding in `visiontools.show_extraction`;
- preserving the answer-checked `7 × 7` feature-map result;
- applying `tf.nn.conv1d` with detrend, average, and Spencer kernels over a time series.

[CustomConvnetsExercise.py](./CustomConvnetsExercise.py) contains the solved Kaggle cells for:

- completing the third convolutional block with two 128-filter layers and max pooling;
- compiling the custom binary classifier with Adam, binary cross-entropy, and binary accuracy;
- adding `Dropout(0.2)` to the dense head;
- preserving the exercise reflection on residual overfitting and the comparison with the tutorial model.

[DataAugmentationExercise.py](./DataAugmentationExercise.py) contains the solved Kaggle cells for:

- visualizing randomized contrast, horizontal flips, width changes, and translations;
- reasoning about which transformations preserve labels in different image domains;
- adding conservative contrast, horizontal-flip, and rotation augmentation to the model;
- building the final batch-normalized 64/128/256-filter ConvNet;
- preserving the final reflection on improved performance and slight remaining overfitting.

### Supplemental practice

[CreateYourFirstSubmissionExercise.py](./CreateYourFirstSubmissionExercise.py) contains the saved flowers competition workflow for:

- loading flower image TFRecords from Kaggle's GCS-backed dataset path;
- preparing labeled and unlabeled `tf.data` pipelines for train, validation, and test splits;
- configuring TPU-aware distribution strategy and batch sizing;
- training a frozen VGG16 feature extractor with a multiclass softmax head;
- using a scheduled learning rate during training;
- writing image IDs and predicted flower labels to `submission.csv`.

[TPUsPlusCassavaLeafDiseaseExercise.py](./TPUsPlusCassavaLeafDiseaseExercise.py) contains the saved cassava leaf-disease competition workflow for:

- reading train, validation, and test TFRecord shards from Kaggle storage;
- parsing `target` labels for training examples and `image_name` IDs for test examples;
- splitting training files into train and validation partitions with `train_test_split`;
- preparing TPU-aware `tf.data` pipelines with repeat, shuffle, batch, cache, and prefetch steps;
- inspecting train, validation, and test batches with Matplotlib helper functions;
- training a frozen ResNet50 feature extractor with a compact five-class softmax head;
- using an exponential learning-rate decay and sparse multiclass metrics;
- writing ordered test predictions to `submission.csv`.

[DetectingtheHiggsBosonWithTPUsExercise.py](./DetectingtheHiggsBosonWithTPUsExercise.py) contains the saved Higgs Boson TPU workflow for:

- reading training and validation TFRecord shards from Kaggle's GCS-backed `higgs-boson` dataset;
- parsing serialized 28-value float feature tensors and binary labels;
- scaling batch size, steps per epoch, and validation steps for the active distribution strategy;
- preparing cached, repeated, shuffled, batched, and prefetched `tf.data` pipelines;
- building a regularized deep network from repeated dense, batch-normalization, activation, and dropout blocks;
- combining the deep network with a `keras.experimental.LinearModel` through `WideDeepModel`;
- compiling with binary cross-entropy, Adam, AUC, binary accuracy, and large `steps_per_execution`;
- using early stopping and plateau-based learning-rate reduction;
- plotting cross-entropy loss and AUC curves from the saved history.

### Execution context

Most exported files are **study evidence, not standalone scripts**. Kaggle supplies objects and infrastructure that are intentionally absent from the official lesson exports, including:

- `pretrained_base`;
- `tf`, `visiontools`, images, kernels, time-series data, and the prepared image datasets;
- training/history cells surrounding the exercise prompts;
- `q_*` objects from Kaggle's answer-checking system.

The supplemental workflows also expect Kaggle notebook context, including `kaggle_datasets`, GCS dataset access, accelerator configuration, competition or hosted datasets, and notebook shell helpers. To reproduce an official exercise, open [the course on Kaggle](https://www.kaggle.com/learn/computer-vision), run its notebook in order, and use the corresponding export as the solved-cell reference. To reproduce a supplemental workflow, run it in a Kaggle notebook attached to the relevant flowers, cassava, or `higgs-boson` dataset.

## Completion Standard

The course completion standard is satisfied: all six official exercise exports and the certificate are present. The supplemental workflows are archived as additional practice.

- [x] The Convolutional Classifier
- [x] Convolution and ReLU
- [x] Maximum Pooling
- [x] The Sliding Window
- [x] Custom ConvNets
- [x] Data Augmentation
- [x] Supplemental flowers submission workflow archived
- [x] Supplemental cassava leaf-disease submission workflow archived
- [x] Supplemental Higgs Boson TPU workflow archived
- [x] Completion certificate archived
- [x] Root roadmap updated from 13/17 to 14/17

## Takeaway

The six lessons establish both levels of the same system: **a vision classifier is a learned feature extractor plus a decision head**, and the extractor is built from local pattern detectors, nonlinear activations, spatial compression, and sliding-window reuse. Transfer learning reuses already learned detectors; convolution explains how each detector scans an image; ReLU turns its responses into composable evidence; maximum pooling keeps strong local responses while reducing spatial cost; the sliding-window lesson makes stride, padding, and shared filters concrete in both 2D images and 1D signals; the custom-ConvNet lesson assembles those operations into a fully trainable hierarchy with dropout in the head; and data augmentation adds plausible input variation as an explicit generalization strategy.

The supplemental workflows add the surrounding competition and accelerator discipline: stream image or tabular TFRecords efficiently, keep the accelerator strategy explicit, preserve test ordering where a submission is required, match softmax output to sparse multiclass image labels, match sigmoid/AUC monitoring to binary tabular labels, and make the final artifact valid for its notebook context.

The engineering discipline is equally important: reason from kernel to feature map, inspect what pooling removes, verify tensor shapes, freeze before fine-tuning, align the output with the loss, apply only label-preserving transformations, trust validation behavior over training performance, and never mistake “less overfit” for “fully fit.”

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Computer%20Vision.png"><img src="./Cux%20Prada%20-%20Computer%20Vision.png" width="600" alt="Computer Vision certificate" /></a>

*Completed June 25, 2026.*

</div>

---

<div align="center">

[← Intro to Deep Learning](../13_IntroToDeepLearning/) · [Back to Roadmap](../README.md) · [Geospatial Analysis →](https://www.kaggle.com/learn/geospatial-analysis)

</div>
