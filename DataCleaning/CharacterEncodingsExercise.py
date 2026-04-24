new_entry = sample_entry.decode("big5-tw").encode()

# Check your answer
q1.check()

# TODO: Load in the DataFrame correctly.
with open("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", "rb") as rawdata:
    result = charset_normalizer.detect(rawdata.read(150000))

print(result)

police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding = "Windows-1252")

# Check your answer
q2.check()

# TODO: Save the police killings dataset to CSV
police_killings.to_csv("my_file.csv")

# Check your answer
q3.check()


