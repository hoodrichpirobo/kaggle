# TODO: Your code here!
earthquakes["Date"].head() # it indeed contain object type dates

# TODO: Your code here
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"

earthquakes["date_parsed"] = pd.to_datetime(earthquakes["Date"], format = "%m/%d/%Y")

# Check your answer
q2.check()

# try to get the day of the month from the date column
day_of_month_earthquakes = earthquakes["date_parsed"].dt.day

# Check your answer
q3.check()

# TODO: Your code here!
day_of_month_earthquakes = day_of_month_earthquakes.dropna()
sns.distplot(day_of_month_earthquakes, kde = False, bins = 31)


