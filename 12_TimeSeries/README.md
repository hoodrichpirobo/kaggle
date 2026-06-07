<div align="center">

# Time Series

**Course 12 of 17 - forecasting by turning the calendar into features: time-step, lag, trend, seasonality, and hybrid models.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Time%20Series-20BEFF.svg)](https://www.kaggle.com/learn/time-series)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![Lessons](https://img.shields.io/badge/Lessons-1%20of%206-blue.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 12 of 17 |
| Estimated time | 5 hours |
| Status | In progress |
| Started | June 7, 2026 |
| Completed | — (in progress) |
| Course page | [Kaggle Learn: Time Series](https://www.kaggle.com/learn/time-series) |

This is the first course of **Phase 5 - Specialized Topics** and the first one in the repo where row order carries information.

## What This Course Adds

[Feature Engineering](../11_FeatureEngineering/) treated rows as independent and focused on building better columns for the model to learn from. Time Series breaks that independence assumption: observations arrive in order, each one is related to the ones before it, and the most useful features are derived from the time index itself rather than collected as separate fields.

The course reframes forecasting as a regression problem on two new feature families - **time-step features** that track where in the series an observation falls, and **lag features** that carry recent values forward - then layers trend, seasonality, and residual modeling on top. It is also the first course where the train/validation boundary is a *moment in time* rather than a random split, because the future must never be used to predict the past.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Linear Regression With Time Series | Complete | [LinearRegressionWithTimeSeriesExercise.py](./LinearRegressionWithTimeSeriesExercise.py) |
| 2 | Trend | Not started | `TrendExercise.py` |
| 3 | Seasonality | Not started | `SeasonalityExercise.py` |
| 4 | Time Series as Features | Not started | `TimeSeriesAsFeaturesExercise.py` |
| 5 | Hybrid Models | Not started | `HybridModelsExercise.py` |
| 6 | Forecasting With Machine Learning | Not started | `ForecastingWithMachineLearningExercise.py` |

Filenames for lessons 2-6 are shown as plain text because those exercises are not solved yet; they follow the repo's `<LessonName>Exercise.py` convention and will become links as each one lands. Every exercise in this course runs on the [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting) competition data (Corporación Favorita grocery sales, Ecuador).

## Forecasting Playbook

The course builds a practical sequence for going from a raw series to a defensible forecast:

1. Plot the series first and read its shape - trend, seasonal cycles, and how strongly each point depends on the ones before it.
2. Build **time-step features** (a time dummy) to model where the series is heading and **lag features** to model how it depends on its own recent past.
3. Fit a deterministic **trend** with linear regression, using moving averages to decide the trend's order.
4. Add **seasonal** structure with seasonal indicators for short cycles and Fourier features for longer ones, choosing frequencies from a periodogram.
5. Turn the past into predictors with **lag features**, using (partial) autocorrelation to pick which lags actually help.
6. Combine forecasters into a **hybrid**: a simple model for trend and season, a second model (e.g. boosted trees) on the residuals it leaves behind.
7. Pick a **multistep strategy** - multioutput, direct, recursive, or DirRec - to forecast a whole horizon rather than a single step.

## Skills Practiced So Far

From the solved lesson 1 exercise:

- Framing a forecast as ordinary regression on features derived from the time index
- Distinguishing the two time-series feature families: time-step features (for trend) and lag features (for serial dependence)
- Building a time dummy with `np.arange(len(df.index))` as a time-step / trend feature
- Fitting `LinearRegression` on a single time-step feature and storing fitted values as a time-indexed `pd.Series`
- Creating a one-step lag feature with `df["sales"].shift(1)`
- Aligning target and lagged features with `y.align(X, join="inner")` and dropping the unmatched first row with `dropna()`
- Reading serial correlation from a lag plot: a smooth, consistent series implies a strong positive lag coefficient (≈ 0.95), an alternating one a strong negative coefficient (≈ -0.95)
- Reasoning about the sign and magnitude of serial dependence directly from a time plot
- Working with the Store Sales `average_sales` series as the course's running dataset
- Preserving written reasoning alongside solved Kaggle answer checks

The granular, course-wide skill list will be backfilled here as lessons 2-6 are completed, in the same style as the [Feature Engineering](../11_FeatureEngineering/#skills-practiced) and [Machine Learning Explainability](../10_MachineLearningExplainability/#skills-practiced) pages.

## On Deck - Remaining Lessons

- **Trend** - model the slow-moving level of a series with moving averages and a time-dummy regression.
- **Seasonality** - capture repeating patterns with seasonal indicators and Fourier features, reading candidate frequencies off a periodogram.
- **Time Series as Features** - predict the future from the past with a lag embedding, choosing lags with the partial autocorrelation function.
- **Hybrid Models** - combine the strengths of two forecasters by fitting one model to trend/season and another to the residuals.
- **Forecasting With Machine Learning** - apply ML to any forecasting task with four multistep strategies: multioutput, direct, recursive, and DirRec.

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [LinearRegressionWithTimeSeriesExercise.py](./LinearRegressionWithTimeSeriesExercise.py) - time-step and lag features fit with `LinearRegression`
- Lessons 2-6 exercises: pending.
- Completion certificate: pending - this course is still in progress.

## Course Notes

- The lesson 1 exercise works with `average_sales`, the mean of `sales` across the Store Sales dataset, framed as a single univariate series to forecast.
- The first two questions are intuition checks done on paper: one is simple arithmetic on a series (`3.33 * 6 ≈ 20`), the other asks to read two lag plots and assign serial-correlation weights - the consistent series gets `+0.95`, the back-and-forth series gets `-0.95`.
- The time-step task builds a trend feature with `time = np.arange(len(df.index))`, fits `LinearRegression` on `X = df[["time"]]` against `y = df["sales"]`, and stores predictions as `pd.Series(model.predict(X), index=X.index)` so the fit stays aligned to the time index.
- The lag task builds `lag_1 = df["sales"].shift(1)`, drops the now-empty first row with `dropna()`, realigns the target with `y, X = y.align(X, join="inner")`, then fits the same `LinearRegression` - the difference is only *which* feature the model sees, not the modeling code.
- Together the two tasks make the core lesson concrete: the exact same regression machinery becomes a trend model or a serial-dependence model purely through the feature you hand it.
- The exported `*Exercise.py` file preserves solved Kaggle notebook cells. It is reference material, not a guaranteed standalone script, because Kaggle provides the dataset, starter variables, plotting helpers, and answer-checking helpers (`q_1.check()`, etc.) inside the notebook environment.

## Notes

This course is where the modeling mindset shifts from "rows are independent samples" to "the series is one object that unfolds in order." The discipline to carry forward: a forecast is only honest if every feature it uses would have been available at the moment the prediction is made, which makes the time-ordered train/validation boundary as important here as leakage control was in the tabular courses.

## Certificate of Completion

<div align="center">

*In progress - the completion certificate will be added here once all six lessons are finished, matching the layout used across the completed courses.*

</div>

<div align="center">

[Back to Roadmap](../README.md)

</div>
