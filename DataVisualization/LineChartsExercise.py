# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col = "Date", parse_dates = True)

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()

# Print the last five rows of the data 
museum_data.tail()

# Fill in the line below: How many visitors did the Chinese American Museum 
# receive in July 2018?
ca_museum_jul18 =  2620

# Fill in the line below: In October 2018, how many more visitors did Avila 
# Adobe receive than the Firehouse Museum?
avila_oct18 = 19280 - 4622

# Check your answers
step_2.check()

# Line chart showing the number of visitors to each museum over time
plt.figure(figsize = (12,6))
sns.lineplot(data = museum_data)
plt.title("Monthly Visitors To Los Angeles City Museums")

# Check your answer
step_3.check()

plt.show()

# Line plot showing the number of visitors to Avila Adobe over time
plt.figure(figsize = (12, 6))
sns.lineplot(data = museum_data["Avila Adobe"], label = "Avila Adobe")
plt.title("Monthly Visitors to Avila Adobe Museum")
plt.xlabel("Date")

# Check your answer
step_4.a.check()

# Avila Adobe gets more visitors in March-August (in LA, the spring and summer)
