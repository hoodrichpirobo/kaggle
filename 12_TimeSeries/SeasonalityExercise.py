# View the solution (Run this cell to receive credit!)
# Strong weekly seasonality, monthly and biweekly too
q_1.check()

y = average_sales.copy()

# YOUR CODE HERE
fourier = CalendarFourier(freq = "M", order = 4)
dp = DeterministicProcess(
    index=y.index,
    constant=True,
    order=1,
    # YOUR CODE HERE
    seasonal = True,
    additional_terms = [fourier],
    drop=True,
)
X = dp.in_sample()

# Check your answer
q_2.check()

# View the solution (Run this cell to receive credit!)
# periodogram for deseasonalized series lacks any large values. Our model was able to capture seasonal variation
q_3.check()

# YOUR CODE HERE
X_holidays = pd.get_dummies(holidays)

X2 = X.join(X_holidays, on='date').fillna(0.0)

# Check your answer
q_4.check()


