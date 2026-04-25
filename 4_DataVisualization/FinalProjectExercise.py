# Fill in the line below: Specify the path of the CSV file to read
my_filepath = "/kaggle/input/datasets/organizations/fivethirtyeight/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"

# Check for a valid filepath to a CSV file in a dataset
step_2.check()

# Fill in the line below: Read the file into a variable my_data
my_data = pd.read_csv(my_filepath, index_col = "page_id")

# Check that a dataset has been uploaded into my_data
step_3.check()

## Create a plot
sns.scatterplot(x = my_data["YEAR"], y = my_data["APPEARANCES"], hue = my_data["SEX"])
plt.title("DC Comic Characters Appearances Over Time by Sex")

# Check that a figure appears below
step_4.check()
