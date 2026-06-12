<div align="center">

# Time Series

**Course 12 of 17 - forecasting by turning the calendar into features: time-step, lag, trend, seasonality, and hybrid models.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Time%20Series-20BEFF.svg)](https://www.kaggle.com/learn/time-series)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-6%20of%206-brightgreen.svg)

</div>

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 12 of 17 |
| Estimated time | 5 hours |
| Status | Complete |
| Started | June 7, 2026 |
| Completed | June 12, 2026 |
| Course page | [Kaggle Learn: Time Series](https://www.kaggle.com/learn/time-series) |

This is the first course of **Phase 5 - Specialized Topics** and the first one in the repo where row order carries information.

## What This Course Adds

[Feature Engineering](../11_FeatureEngineering/) treated rows as independent and focused on building better columns for the model to learn from. Time Series breaks that independence assumption: observations arrive in order, each one is related to the ones before it, and the most useful features are derived from the time index itself rather than collected as separate fields.

The course reframes forecasting as a regression problem on two new feature families - **time-step features** that track where in the series an observation falls, and **lag features** that carry recent values forward - then layers trend, seasonality, and residual modeling on top. It is also the first course where the train/validation boundary is a *moment in time* rather than a random split, because the future must never be used to predict the past.

## Lesson Tracker

| # | Lesson | Status | Exercise |
|:-:|--------|:------:|:--------:|
| 1 | Linear Regression With Time Series | Complete | [LinearRegressionWithTimeSeriesExercise.py](./LinearRegressionWithTimeSeriesExercise.py) |
| 2 | Trend | Complete | [TrendExercise.py](./TrendExercise.py) |
| 3 | Seasonality | Complete | [SeasonalityExercise.py](./SeasonalityExercise.py) |
| 4 | Time Series as Features | Complete | [TimeSeriesAsFeaturesExercise.py](./TimeSeriesAsFeaturesExercise.py) |
| 5 | Hybrid Models | Complete | [HybridModelsExercise.py](./HybridModelsExercise.py) |
| 6 | Forecasting With Machine Learning | Complete | [ForecastingWithMachineLearningExercise.py](./ForecastingWithMachineLearningExercise.py) |

Every exercise in this course runs on the [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting) competition data (Corporación Favorita grocery sales, Ecuador).

## Forecasting Playbook

The course builds a practical sequence for going from a raw series to a defensible forecast:

1. Plot the series first and read its shape - trend, seasonal cycles, and how strongly each point depends on the ones before it.
2. Build **time-step features** (a time dummy) to model where the series is heading and **lag features** to model how it depends on its own recent past.
3. Fit a deterministic **trend** with linear regression, using moving averages to decide the trend's order.
4. Add **seasonal** structure with seasonal indicators for short cycles and Fourier features for longer ones, choosing frequencies from a periodogram.
5. Turn the past into predictors with **lag features**, using (partial) autocorrelation to pick which lags actually help.
6. Combine forecasters into a **hybrid**: a simple model for trend and season, a second model (e.g. boosted trees) on the residuals it leaves behind.
7. Pick a **multistep strategy** - multioutput, direct, recursive, or DirRec - to forecast a whole horizon rather than a single step.

## Skills Practiced

From the six solved exercises:

- Framing a forecast as ordinary regression on features derived from the time index
- Distinguishing the two time-series feature families: time-step features (for trend) and lag features (for serial dependence)
- Building a time dummy with `np.arange(len(df.index))` as a time-step / trend feature
- Fitting `LinearRegression` on a single time-step feature and storing fitted values as a time-indexed `pd.Series`
- Creating a one-step lag feature with `df["sales"].shift(1)`
- Aligning target and lagged features with `y.align(X, join="inner")` and dropping the unmatched first row with `dropna()`
- Reading serial correlation from a lag plot: a smooth, consistent series implies a strong positive lag coefficient (≈ 0.95), an alternating one a strong negative coefficient (≈ -0.95)
- Reasoning about the sign and magnitude of serial dependence directly from a time plot
- Working with the Store Sales `average_sales` series as the course's running dataset
- Estimating slow-moving trend with centered rolling averages
- Choosing moving-average parameters with `rolling(window=12, center=True, min_periods=6).mean()`
- Reading trend shape from a smoothed series before committing to a model order
- Recognizing a quadratic-looking bend in the food-sales trend
- Creating polynomial trend features with `statsmodels.tsa.deterministic.DeterministicProcess`
- Building a cubic trend design matrix with `DeterministicProcess(index=average_sales.index, order=3)`
- Generating in-sample trend features with `dp.in_sample()`
- Generating a 90-day future trend feature matrix with `dp.out_of_sample(steps=90)`
- Treating long-horizon polynomial extrapolation with caution because the forecast can deviate sharply when the assumed trend order is wrong
- Reading a periodogram to identify strong seasonal frequencies before choosing seasonal features
- Recognizing weekly seasonality as the dominant repeating pattern in the Store Sales average-sales series, with additional monthly and biweekly signal
- Building a combined deterministic feature matrix with `DeterministicProcess`
- Adding a constant, linear trend, seasonal indicators, and Fourier terms in one design matrix
- Creating monthly Fourier features with `CalendarFourier(freq="M", order=4)`
- Using `seasonal=True` for calendar-seasonal indicators alongside Fourier features
- Calling `dp.in_sample()` to generate the training feature matrix for the full observed date index
- Checking a deseasonalized periodogram to confirm that the chosen seasonal model absorbed the main repeating variation
- One-hot encoding holiday/event labels with `pd.get_dummies(holidays)`
- Joining holiday indicators onto the deterministic feature matrix by date with `X.join(X_holidays, on="date").fillna(0.0)`
- Treating holidays and special events as calendar regressors separate from trend and recurring seasonality
- Smoothing a target series with `y.rolling(window=7, center=True).mean()` before reading short-term dependence
- Using lag plots and partial autocorrelation to choose useful target lags instead of blindly adding every recent value
- Reading the exercise's lag evidence as strongest around lags 8 and 1, with a mostly linear effect
- Separating autoregressive target signal from known external drivers such as promotion schedules
- Building lagged target features from a deseasonalized series with `make_lags(y_deseason, lags=1)`
- Combining lagged, current, and leading promotion features with `pd.concat`
- Using `make_leads(onpromotion, leads=1)` only because planned promotions are known ahead of the forecast date
- Dropping incomplete rows after lead/lag construction with `.dropna()` and realigning target/features with `y.align(X, join="inner")`
- Building rolling-window summaries from a shifted target, including a 7-day mean, 14-day median, and 7-day standard deviation
- Creating centered rolling promotion counts with `onpromo.rolling(7, center=True).sum()` for known-in-advance covariates
- Guarding against leakage by rolling lagged target values, while allowing future-looking features only when they would truly be available at prediction time
- Implementing a boosted hybrid forecaster that trains one model on baseline forecasting features and a second model on the first model's residuals
- Fitting `model_1` on `X_1` and the wide target matrix `y`, then storing its fitted values as a DataFrame aligned to `X_1.index` and `y.columns`
- Computing residual targets with `y - y_fit` before handing unexplained structure to the second-stage model
- Converting wide residuals to long form with `.stack().squeeze()` so the residual model can learn row-level corrections
- Saving `y_columns`, `y_fit`, and `y_resid` on the hybrid model to keep fit diagnostics and prediction reshaping consistent
- Building hybrid predictions by stacking the first-stage forecast, adding `model_2.predict(X_2)`, and unstacking back to the original wide target layout
- Combining `LinearRegression` for trend/season baseline structure with `XGBRegressor` for nonlinear residual structure
- Clipping final Store Sales forecasts at `0.0` so predicted sales respect the nonnegative target domain
- Defining forecast origin, forecast horizon, lead time, and forecast steps for a competition test window
- Matching forecasting strategy to task shape: single-step, multistep sequence, and multiseries forecasting
- Selecting `family_sales.loc[:, "sales"]` as a wide multi-family target matrix for supervised forecasting
- Creating four target-lag features with `make_lags(y, lags=4).dropna()`
- Creating a 16-step multistep target matrix with `make_multistep_target(y, steps=16).dropna()`
- Aligning lagged features and multistep targets with `y.align(X, join="inner", axis=0)`
- Using `RegressorChain(XGBRegressor())` as a DirRec-style forecaster that feeds earlier predicted steps into later ones
- Reading the Store Sales test dates to derive `forecast_start` and `n_steps` from the actual submission horizon
- Extending the observed target index with a one-day future period so the first forecast row can be lagged from the final training observations
- Building the submission feature row from lagged wide targets, stacking by product family, and label-encoding the `family` feature
- Predicting all 16 forecast steps, clipping negative sales to zero, and reshaping the wide forecast back to long `date` / `family` rows
- Joining predicted sales back to Kaggle test `id` values and writing `submission.csv`
- Treating Store Sales forecasting as a full competition workflow, not just an in-sample model check
- Preserving written reasoning alongside solved Kaggle answer checks

## Artifacts

- Exercise solutions exported as Python files for quick review:
  - [LinearRegressionWithTimeSeriesExercise.py](./LinearRegressionWithTimeSeriesExercise.py) - time-step and lag features fit with `LinearRegression`
  - [TrendExercise.py](./TrendExercise.py) - centered moving averages and polynomial trend features with `DeterministicProcess`
  - [SeasonalityExercise.py](./SeasonalityExercise.py) - seasonal indicators, Fourier features, and holiday regressors
  - [TimeSeriesAsFeaturesExercise.py](./TimeSeriesAsFeaturesExercise.py) - lag/lead embeddings, rolling summaries, and known-in-advance promotion features
  - [HybridModelsExercise.py](./HybridModelsExercise.py) - two-stage `LinearRegression` plus `XGBRegressor` hybrid over residuals
  - [ForecastingWithMachineLearningExercise.py](./ForecastingWithMachineLearningExercise.py) - lagged wide targets, 16-step multistep forecasting, `RegressorChain`, and Kaggle submission formatting
- Completion certificate: [Cux Prada - Time Series.png](./Cux%20Prada%20-%20Time%20Series.png)

## Course Notes

- The lesson 1 exercise works with `average_sales`, the mean of `sales` across the Store Sales dataset, framed as a single univariate series to forecast.
- The first two questions are intuition checks done on paper: one is simple arithmetic on a series (`3.33 * 6 ≈ 20`), the other asks to read two lag plots and assign serial-correlation weights - the consistent series gets `+0.95`, the back-and-forth series gets `-0.95`.
- The time-step task builds a trend feature with `time = np.arange(len(df.index))`, fits `LinearRegression` on `X = df[["time"]]` against `y = df["sales"]`, and stores predictions as `pd.Series(model.predict(X), index=X.index)` so the fit stays aligned to the time index.
- The lag task builds `lag_1 = df["sales"].shift(1)`, drops the now-empty first row with `dropna()`, realigns the target with `y, X = y.align(X, join="inner")`, then fits the same `LinearRegression` - the difference is only *which* feature the model sees, not the modeling code.
- Together the two tasks make the core lesson concrete: the exact same regression machinery becomes a trend model or a serial-dependence model purely through the feature you hand it.
- The trend exercise starts with a centered 12-period moving average on `food_sales`, using `min_periods=6` so the smoothed trend remains defined near the edges of the series.
- The saved trend-reading answer identifies an upward bend in the smoothed food-sales line, making a quadratic trend the natural visual fit for that series.
- The polynomial-trend task uses `DeterministicProcess(index=average_sales.index, order=3)` to create a cubic time basis, then calls `dp.in_sample()` for the training rows and `dp.out_of_sample(steps=90)` for a 90-day forecast horizon.
- The final trend note records the main risk of polynomial extrapolation: if the chosen trend shape is wrong, the forecast can move far away from the real series very quickly.
- The seasonality exercise starts from the periodogram: the strongest recurring pattern is weekly, with monthly and biweekly components also visible enough to model.
- Its deterministic seasonal design combines `constant=True`, `order=1`, `seasonal=True`, and `CalendarFourier(freq="M", order=4)` inside one `DeterministicProcess`, then calls `dp.in_sample()` to build `X`.
- The deseasonalized periodogram check records that no large seasonal spikes remain, which is the evidence that the model captured the major seasonal variation.
- Holiday and event effects are added as one-hot regressors with `pd.get_dummies(holidays)`, then joined to the seasonal feature matrix on `date` and filled with `0.0` so non-holiday rows stay explicit.
- The time-series-as-features exercise opens by smoothing `y` with a centered seven-day moving average, making weekly local structure easier to see before building predictors.
- Its written lag-reading answer records lags 8 and 1 as useful candidates and notes that the relationship looks mostly linear.
- The promotion-feature answer keeps both lagged and leading values in play: lagged promotions can capture after-effects, while leading promotions are legitimate only because promotion schedules are known before the forecast date.
- The main feature matrix combines `make_lags(y_deseason, lags=1)` with lagged, current, and one-step-leading `onpromotion` values, then uses `.dropna()` and `y.align(X, join="inner")` to keep rows consistent.
- The rolling-feature task shifts `supply_sales["sales"]` before summarizing it, then derives a seven-day mean, fourteen-day median, and seven-day standard deviation so the model sees recent level and volatility without peeking at the current target.
- Promotion intensity is summarized separately with a centered seven-day rolling sum on `onpromotion`, which is safe here because planned promotions are a future-known covariate rather than an observed target value.
- The hybrid-models exercise implements `BoostedHybrid.fit` as a two-stage residual workflow: `model_1.fit(X_1, y)` creates the baseline forecast, `y - y_fit` becomes the residual target, and `model_2.fit(X_2, y_resid)` learns the remaining pattern.
- Residuals are converted from the course's wide multi-output target shape into long form with `.stack().squeeze()` before fitting the second model, which lets the residual learner operate on row-level corrections.
- `BoostedHybrid.predict` mirrors the same shape discipline: create a wide baseline prediction, stack it to long form, add the second-stage residual prediction, then `unstack()` back to the original target columns.
- The final hybrid combines `LinearRegression()` with `XGBRegressor()`, fits on `X_1`, `X_2`, and `y`, predicts in sample for the exercise check, and clips the result at `0.0` to keep sales forecasts physically valid.
- The lesson's practical takeaway is model decomposition: use a simple, interpretable forecaster for broad trend/season structure, then let a more flexible learner focus only on the residual signal that remains.
- The forecasting-with-machine-learning exercise starts by distinguishing forecast origin, forecast horizon, lead time, and forecast steps against the Store Sales split: the origin is August 15, 2017, and the test horizon runs from August 16 through August 31, 2017.
- The strategy-matching answer maps different forecasting tasks to the appropriate setup, separating single-step forecasting, multi-step forecasting, and multi-series forecasting.
- The main supervised setup selects the wide `family_sales["sales"]` matrix, creates four lag features with `make_lags`, creates a 16-step target with `make_multistep_target`, then aligns both objects on the same dates before fitting.
- `RegressorChain(XGBRegressor())` is used for the final multistep model, giving a DirRec-style chain where each predicted step can become context for later predicted steps.
- The submission section reads the real test dates, builds the first forecast feature row from the final observed lags, stacks product families into rows, label-encodes `family`, predicts all 16 days, clips negative values, reshapes back to long format, merges with Kaggle test IDs, and writes `submission.csv`.
- The final lesson's practical takeaway is that forecasting strategy is part of the model design: the target shape, horizon length, and known-at-prediction features determine whether a simple one-step model is enough or a multistep strategy is required.
- The exported `*Exercise.py` file preserves solved Kaggle notebook cells. It is reference material, not a guaranteed standalone script, because Kaggle provides the dataset, starter variables, plotting helpers, and answer-checking helpers (`q_1.check()`, etc.) inside the notebook environment.

## Notes

This course is where the modeling mindset shifts from "rows are independent samples" to "the series is one object that unfolds in order." The discipline to carry forward: a forecast is only honest if every feature it uses would have been available at the moment the prediction is made, which makes the time-ordered train/validation boundary as important here as leakage control was in the tabular courses.

The other carry-forward habit is choosing the forecasting strategy from the horizon itself. One-step, direct, recursive, DirRec, and multioutput forecasts are not interchangeable wrappers; they encode different assumptions about how predictions depend on one another across future dates.

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Time%20Series.png"><img src="./Cux%20Prada%20-%20Time%20Series.png" width="600" alt="Time Series certificate" /></a>

*Completed June 12, 2026.*

</div>

<div align="center">

[Back to Roadmap](../README.md)

</div>
