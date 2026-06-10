# YOUR CODE HERE
y_ma = y.rolling(window = 7, center = True).mean()


# Plot
ax = y_ma.plot()
ax.set_title("Seven-Day Moving Average");

# Check your answer
q_1.check()

# View the solution (Run this cell to receive credit!)
# Lag 8 and 1, it suggests the effect is mostly linear
q_2.check()

# both leading and lagged values could be useful
q_3.check()

# YOUR CODE HERE: Make features from `y_deseason`
X_lags = make_lags(y_deseason, lags = 1)

# YOUR CODE HERE: Make features from `onpromotion`
# You may want to use `pd.concat`
X_promo = pd.concat([
    make_lags(onpromotion, lags = 1),
    onpromotion,
    make_leads(onpromotion, leads = 1),
], axis = 1)

X = pd.concat([X_lags, X_promo], axis=1).dropna()
y, X = y.align(X, join='inner')

# Check your answer
q_4.check()

y_lag = supply_sales.loc[:, 'sales'].shift(1)
onpromo = supply_sales.loc[:, 'onpromotion']

# 28-day mean of lagged target
mean_7 = y_lag.rolling(7).mean()
# YOUR CODE HERE: 14-day median of lagged target
median_14 = y_lag.rolling(14).median()
# YOUR CODE HERE: 7-day rolling standard deviation of lagged target
std_7 = y_lag.rolling(7).std()
# YOUR CODE HERE: 7-day sum of promotions with centered window
promo_7 = onpromo.rolling(7, center = True).sum()


# Check your answer
q_5.check()


