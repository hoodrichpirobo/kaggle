# Path of the files to read
cancer_filepath = "../input/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = pd.read_csv(cancer_filepath, index_col = "Id")

# Run the line below with no changes to check that you've loaded the data correctly
step_1.check()

# Print the first five rows of the data
cancer_data.head()

# Fill in the line below: In the first five rows of the data, what is the
# largest value for 'Perimeter (mean)'?
max_perim = 87.46

# Fill in the line below: What is the value for 'Radius (mean)' for the tumor with Id 8510824?
mean_radius = 9.504

# Check your answers
step_2.check()

# Histograms for benign and maligant tumors
sns.histplot(data = cancer_data, x = "Area (mean)", hue = "Diagnosis")

# Check your answer
step_3.a.check()

# Malignant tumors have higher values for 'Area (mean)' (relative to benign tumors), on average
# Malignant

# KDE plots for benign and malignant tumors
sns.kdeplot(data = cancer_data, x = "Radius (worst)", hue = "Diagnosis", shade = True)

# Check your answer
step_4.a.check()

# as malignant


