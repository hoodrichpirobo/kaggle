# TODO: Your code here!
sf_permits.head()

# TODO: Your code here!
total_cells = np.product(sf_permits.shape)
total_missing = sf_permits.isnull().sum().sum()
percent_missing = (total_missing / total_cells) * 100

# Check your answer
q2.check()

# not all addresses have a suffix, so they might not exist. But all addresses have a zipcode, so they have not been recorded.

# TODO: Your code here!
sf_permits.dropna()

# TODO: Your code here
sf_permits_with_na_dropped = sf_permits.dropna(axis = 1)

dropped_columns = sf_permits.shape[1] - sf_permits_with_na_dropped.shape[1]

# Check your answer
q5.check()

# TODO: Your code here
sf_permits_with_na_imputed = sf_permits.fillna(method = "bfill", axis = 0).fillna(0)

# Check your answer
q6.check()


