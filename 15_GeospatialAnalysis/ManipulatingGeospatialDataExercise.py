# Create the geocoder
geolocator = Nominatim(user_agent="kaggle_learn")

# Your code here
def my_geocoder(row):
    point = geolocator.geocode(row).point
    return pd.Series({"Latitude": point.latitude, "Longitude" : point.longitude})

berkeley_locations = rows_with_missing.apply(lambda x: my_geocoder(x["Address"]), axis = 1)
starbucks.update(berkeley_locations)

# Check your answer
q_1.check()

# Create a base map
m_2 = folium.Map(location=[37.88,-122.26], zoom_start=13)

# Your code here: Add a marker for each Berkeley location
for idx, row in starbucks[starbucks["City"] == "Berkeley"].iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup = row["Store Name"]).add_to(m_2)

# Uncomment to see a hint
#q_2.a.hint()

# Show the map
embed_map(m_2, 'q_2.html')

# View the solution (Run this code cell to receive credit!)
# all of them
q_2.b.solution()

# Your code here
CA_stats = CA_counties.merge(CA_pop, on = "GEOID")
CA_stats = CA_stats.merge(CA_high_earners, on = "GEOID")
CA_stats = CA_stats.merge(CA_median_age, on = "GEOID")


# Check your answer
q_3.check()

# Your code here
sel_counties = CA_stats[((CA_stats.high_earners > 100000) &
                         (CA_stats.median_age < 38.5) &
                         (CA_stats.density > 285) &
                         ((CA_stats.median_age < 35.5) |
                         (CA_stats.density > 1400) |
                         (CA_stats.high_earners > 500000)))]
# Check your answer
q_4.check()

# Fill in your answer
num_stores = len(gpd.sjoin(starbucks_gdf, sel_counties))

# Check your answer
q_5.check()

# Create a base map
m_6 = folium.Map(location=[37,-120], zoom_start=6)

# Your code here: show selected store locations
for idx, row in gpd.sjoin(starbucks_gdf, sel_counties).iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup = row["Store Name"]).add_to(m_6)

# Uncomment to see a hint
q_6.hint()

# Show the map
embed_map(m_6, 'q_6.html')
