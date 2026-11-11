
# Load historical vaccination data
vaccinationData = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv"
)

# Convert dates into datetime objects
vaccinationData["date"] = pd.to_datetime(
    vaccinationData["date"]
)

# Get the latest available non-null record for each location
vaccinationByLocation = (
    vaccinationData
    .dropna(subset=["people_vaccinated"])
    .sort_values("date")
    .drop_duplicates(subset=["location"], keep="last")
    [["location", "people_vaccinated"]]
)

print("Latest dataset date:", vaccinationData["date"].max())

