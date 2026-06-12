# YOUR CODE HERE: Match the task to the dataset. Answer 1, 2, or 3.
task_a = 2
task_b = 1
task_c = 3

# Check your answer
q_1.check()

# View the solution (Run this cell to receive credit!)
# Forecast origin is the last training date, 2017-8-15. Forecast horizon is the range of Test Data, 2017-08-16 to 2017-08-31. 
# There is one step within the forecast horizon.
# Lead time is the amount of days between forecast origin and first date of Test data, 1 step. 
q_2.check()

# YOUR CODE HERE
y = family_sales.loc[:, 'sales']

# YOUR CODE HERE: Make 4 lag features
X = make_lags(y, lags = 4).dropna()

# YOUR CODE HERE: Make multistep target
y = make_multistep_target(y, steps = 16).dropna()

y, X = y.align(X, join='inner', axis=0)

# Check your answer
q_3.check()

from sklearn.multioutput import RegressorChain

# YOUR CODE HERE
model = RegressorChain(XGBRegressor())

# Check your answer
q_4.check()

test_dates = test.index.get_level_values("date").unique().sort_values()
forecast_start = test_dates.min()
n_steps = len(test_dates)

print("Forecast start:", forecast_start)
print("Forecast horizon steps:", n_steps)

y_full = family_sales.loc[:, "sales"]

future_index = pd.period_range(
    start=y_full.index.max() + 1,
    periods=1,
    freq="D",
)

y_extended = y_full.reindex(y_full.index.union(future_index))

X_submit = make_lags(y_extended, lags=4).loc[[forecast_start]]

X_submit = (
    X_submit
    .stack("family")
    .reset_index("family")
)

submit_families = X_submit["family"].copy()

X_submit["family"] = le.transform(X_submit["family"])

X_submit = X_submit[X.columns]

y_submit_pred = pd.DataFrame(
    model.predict(X_submit),
    index=pd.MultiIndex.from_arrays(
        [[forecast_start] * len(submit_families), submit_families],
        names=["date", "family"]
    ),
    columns=y.columns,
).clip(0.0)

pred_long = (
    y_submit_pred
    .stack()
    .rename("sales")
    .reset_index()
    .rename(columns={"level_2": "step"})
)

pred_long["step_num"] = pred_long["step"].str.extract(r"(\d+)").astype(int)
pred_long["date"] = pred_long["step_num"].apply(lambda s: test_dates[s - 1])

pred_long = pred_long[["date", "family", "sales"]]

submission = (
    test.reset_index()[["id", "date", "family"]]
    .merge(pred_long, on=["date", "family"], how="left")
    [["id", "sales"]]
)

submission["sales"] = submission["sales"].fillna(0).clip(lower=0)

submission.to_csv("submission.csv", index=False)

submission.head()
