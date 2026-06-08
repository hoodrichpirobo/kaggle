# YOUR CODE HERE: Add methods to `food_sales` to compute a moving
# average with appropriate parameters for trend estimation.
trend = food_sales.rolling(
    window = 12,
    center = True,
    min_periods = 6,
).mean()

# Check your answer
q_1.check()

# Make a plot
ax = food_sales.plot(**plot_params, alpha=0.5)
ax = trend.plot(ax=ax, linewidth=3)

# View the solution (Run this cell to receive credit!)
# 2, upwards bend in the trend suggest a quadratic
q_2.check()

from statsmodels.tsa.deterministic import DeterministicProcess

y = average_sales.copy()  # the target

# YOUR CODE HERE: Instantiate `DeterministicProcess` with arguments
# appropriate for a cubic trend model
dp = DeterministicProcess(
    index = average_sales.index,
    order = 3,
)

# YOUR CODE HERE: Create the feature set for the dates given in y.index
X = dp.in_sample()

# YOUR CODE HERE: Create features for a 90-day forecast.
X_fore = dp.out_of_sample(steps = 90)


# Check your answer
q_3.check()

# View the solution (Run this cell to receive credit!)
# it can make huge deviation with wrong predictions
q_4.check()


