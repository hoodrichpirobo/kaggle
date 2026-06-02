<div align="center">

# Feature Engineering

**Course 11 of 17 - turning raw columns into model-ready signal with mutual information, feature creation, clustering, PCA, and target encoding.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Feature%20Engineering-20BEFF.svg)](https://www.kaggle.com/learn/feature-engineering)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-3%20of%206-yellow.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 11 of 17 |
| Estimated time | 5 hours |
| Status | In progress |
| Started | June 1, 2026 |
| Completed | In progress |
| Course page | [Kaggle Learn: Feature Engineering](https://www.kaggle.com/learn/feature-engineering) |

## What This Course Adds

[Machine Learning Explainability](../10_MachineLearningExplainability/) made trained models inspectable: feature importance, partial dependence, and SHAP helped answer what a model learned and whether its behavior made sense. This course moves one step earlier in the workflow: improving the columns the model gets to learn from in the first place.

The central idea is that useful models rarely depend only on raw fields as collected. A good feature-engineering pass ranks signal, exposes relationships, compresses redundant structure, creates interaction-friendly columns, and encodes categories without leaking target information into validation or test data.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | What Is Feature Engineering | Complete | Tutorial |
| 2 | Mutual Information | Complete | [MutualInformationExercise.py](./MutualInformationExercise.py) |
| 3 | Creating Features | Complete | [CreatingFeaturesExercise.py](./CreatingFeaturesExercise.py) |
| 4 | Clustering With K-Means | Not started | Pending |
| 5 | Principal Component Analysis | Not started | Pending |
| 6 | Target Encoding | Not started | Pending |

## Feature Engineering Playbook

The course builds a practical workflow for finding and creating better tabular features:

1. Start with a clear prediction target and a clean train/validation boundary.
2. Score candidate features with mutual information to find direct signal worth investigating.
3. Use plots to check whether high-scoring columns have learnable relationships with the target.
4. Create features that express ratios, counts, combinations, group indicators, or domain-specific structure more directly than the raw inputs.
5. Add unsupervised features from clustering when row segments carry useful predictive context.
6. Use PCA to summarize correlated numeric columns or discover hidden axes of variation.
7. Apply target encoding carefully, using validation-aware or cross-fold strategies to avoid leakage.
8. Re-evaluate engineered features with model validation rather than trusting intuition alone.

## Skills Practiced

- Framing feature engineering as a modeling-feedback loop instead of one-off column tinkering
- Distinguishing raw fields from model-ready features
- Using mutual information to measure how much a feature tells us about a target
- Ranking numeric and categorical predictors by supervised signal
- Handling discrete features correctly before computing mutual information
- Reading high and low mutual-information scores as investigation prompts, not final proof
- Plotting top-ranked features against `SalePrice` to inspect relationships visually
- Comparing candidate features across `BldgType` facets with `sns.lmplot`
- Identifying `YearBuilt` as a strong signal in the housing data
- Testing whether `GrLivArea` and `MoSold` interact with building type
- Creating ratio features such as living-area-to-lot-area and square-feet-per-room
- Combining related porch and deck columns into aggregate exterior-space features
- Building one-hot interaction features by multiplying building-type indicators by `GrLivArea`
- Counting active porch types with boolean comparisons and row-wise sums
- Splitting mixed categorical codes such as `MSSubClass` into cleaner class features
- Using grouped `transform("median")` to add neighborhood-level living-area context
- Preserving written reasoning alongside solved Kaggle answer checks
- Keeping leakage risk in view while preparing for target-based encodings later in the course

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [MutualInformationExercise.py](./MutualInformationExercise.py)
  - [CreatingFeaturesExercise.py](./CreatingFeaturesExercise.py)
- Upcoming exercise exports will be added as the course progresses:
  - `ClusteringWithKMeansExercise.py`
  - `PrincipalComponentAnalysisExercise.py`
  - `TargetEncodingExercise.py`
- Completion certificate will be added after the course is finished.

## Course Notes

- The mutual-information exercise starts from precomputed `mi_scores`, then inspects the strongest and weakest twenty features.
- `plot_mi_scores(mi_scores.head(20))` is used to make the strongest supervised signals easy to compare.
- `plot_mi_scores(mi_scores.tail(20))` is preserved as a low-signal check, which is useful because weak individual features can still matter through interactions.
- The saved answer records `YearBuilt` as a high-value feature for the housing target.
- The exercise uses `sns.lmplot` with `hue="BldgType"` and `col="BldgType"` to compare feature-target relationships inside building-type groups.
- `GrLivArea` is inspected as a size signal with a clear relationship to `SalePrice`.
- `MoSold` is inspected as a calendar feature whose signal depends more on interaction and context than on a simple linear trend.
- The written answer notes that `GrLivArea` has a linear relationship with sale price and interacts with `BldgType`.
- The creating-features exercise adds direct transformations: `LivLotRatio`, `Spaciousness`, and `TotalOutsideSF` make existing housing measurements easier for a model to use.
- Building-type interactions are encoded by one-hot encoding `BldgType` with `pd.get_dummies(..., prefix="Bldg")`, then multiplying each indicator by `GrLivArea`.
- Porch structure is summarized with `PorchTypes`, a row-wise count of positive porch/deck component columns.
- `MSClass` is extracted from `MSSubClass` by splitting the mixed code string before the first underscore.
- `MedNhbdArea` uses `groupby("Neighborhood")["GrLivArea"].transform("median")` so every row carries neighborhood-scale size context.
- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, starter variables, plotting helpers, and answer-checking helpers inside the notebook environment.

## Notes

This course is the bridge between trustworthy modeling workflows and stronger leaderboard performance. The important habit is discipline: every engineered feature should either make a relationship easier for the model to learn, expose useful structure, or reduce noise, and every gain should survive the same validation rules used by the rest of the pipeline.

## Certificate of Completion

Certificate pending course completion.

<div align="center">

[Back to Roadmap](../README.md)

</div>
