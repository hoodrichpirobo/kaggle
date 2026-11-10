m_1 = folium.Map(location=[40.7, -74], zoom_start=11) 

# Your code here: Visualize the collision data
HeatMap(data = collisions[["LATITUDE", "LONGITUDE"]], radius = 15).add_to(m_1)
for idx, row in collisions.iterrows():
    Marker([row["LATITUDE"], row["LONGITUDE"]]).add_to(m_1)

# Uncomment to see a hint
q_1.hint()

# Show the map
embed_map(m_1, "q_1.html")

m_2 = folium.Map(location=[40.7, -74], zoom_start=11) 

# Your code here: Visualize the hospital locations
HeatMap(data = hospitals[['latitude', 'longitude']], radius = 15).add_to(m_2)
for idx, row in hospitals.iterrows():
    Marker([row['latitude'], row['longitude']]).add_to(m_2)

# Uncomment to see a hint
q_2.hint()
        
# Show the map
embed_map(m_2, "q_2.html")

# Your code here
# outside_range = hospitals.geometry.buffer(10000)
# my_outside_range = outside_range.geometry.unary_union
# sum = 0
# for i in range(len(collisions)):
#     if sum > 0: break
#     sum += my_outside_range.contains(collisions.iloc[i].geometry)

# print(sum)

coverage = gpd.GeoDataFrame(geometry = hospitals.geometry).buffer(10000)
my_union = coverage.geometry.unary_union
outside_range = collisions.loc[~collisions["geometry"].apply(lambda x: my_union.contains(x))]

# Check your answer
q_3.check()

def best_hospital(collision_location):
    # Your code here
    distances = hospitals.geometry.distance(collision_location)
    name = hospitals.iloc[distances.idxmin()]['name']
    return name

# Test your function: this should suggest CALVARY HOSPITAL INC
print(best_hospital(outside_range.geometry.iloc[0]))

# Check your answer
q_4.check()

# Your code here
# counts = {}
# for i in range(len(outside_range)):
#     hospital = best_hospital(outside_range.geometry.iloc[i])
#     counts[hospital] = counts.get(hospital, 0) + 1

# print(counts)

# highest_demand = 'JAMAICA HOSPITAL MEDICAL CENTER'

highest_demand = outside_range.geometry.apply(best_hospital).value_counts().idxmax()

# Check your answer
q_5.check()

# Your answer here: proposed location of hospital 1 Latitude: 40.6598 Longitude: -73.7567
lat_1 = 40.6598
long_1 = -73.7567

# Your answer here: proposed location of hospital 2 Latitude: 40.6702 Longitude: -73.8611
lat_2 = 40.6702
long_2 = -73.8611


# Do not modify the code below this line
try:
    new_df = pd.DataFrame(
        {'Latitude': [lat_1, lat_2],
         'Longitude': [long_1, long_2]})
    new_gdf = gpd.GeoDataFrame(new_df, geometry=gpd.points_from_xy(new_df.Longitude, new_df.Latitude))
    new_gdf.crs = {'init' :'epsg:4326'}
    new_gdf = new_gdf.to_crs(epsg=2263)
    # get new percentage
    new_coverage = gpd.GeoDataFrame(geometry=new_gdf.geometry).buffer(10000)
    new_my_union = new_coverage.geometry.unary_union
    new_outside_range = outside_range.loc[~outside_range["geometry"].apply(lambda x: new_my_union.contains(x))]
    new_percentage = round(100*len(new_outside_range)/len(collisions), 2)
    print("(NEW) Percentage of collisions more than 10 km away from the closest hospital: {}%".format(new_percentage))
    # Did you help the city to meet its goal?
    q_6.check()
    # make the map
    m = folium.Map(location=[40.7, -74], zoom_start=11) 
    folium.GeoJson(coverage.geometry.to_crs(epsg=4326)).add_to(m)
    folium.GeoJson(new_coverage.geometry.to_crs(epsg=4326)).add_to(m)
    for idx, row in new_gdf.iterrows():
        Marker([row['Latitude'], row['Longitude']]).add_to(m)
    HeatMap(data=new_outside_range[['LATITUDE', 'LONGITUDE']], radius=9).add_to(m)
    folium.LatLngPopup().add_to(m)
    display(embed_map(m, 'q_6.html'))
except:
    q_6.hint()


