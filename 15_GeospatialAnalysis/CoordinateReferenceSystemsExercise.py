# Your code here: Create the GeoDataFrame
birds = gpd.GeoDataFrame(birds_df, geometry = gpd.points_from_xy(birds_df["location-long"], birds_df["location-lat"]))
birds.crs = {"init" : "epsg:4326"}

# Your code here: Set the CRS to {'init': 'epsg:4326'}
# birds.crs = ____

# Check your answer
q_1.check()

# Your code here
ax = americas.plot(figsize = (8, 8), color = "whitesmoke", linestyle = ":", edgecolor = "black")
birds.to_crs(epsg = 4326).plot(markersize = 1, ax = ax)

# Uncomment to see a hint
q_2.hint()

# Your code here
end_df = birds.groupby("tag-local-identifier")['geometry'].apply(list).apply(lambda x: x[-1]).reset_index()
end_gdf = gpd.GeoDataFrame(end_df, geometry=end_df.geometry)
end_gdf.crs = {'init' :'epsg:4326'}

# Check your answer
q_3.check()

# Your code here
ax = americas.plot(figsize = (8, 8), color = "white", linestyle = ":", edgecolor = "grey")

start_gdf.plot(ax=ax, color='red',  markersize=30)
path_gdf.plot(ax=ax, cmap='tab20b', linestyle='-', linewidth=1, zorder=1)
end_gdf.plot(ax=ax, color='black', markersize=30)

# Uncomment to see a hint
q_4.hint()

# Path of the shapefile to load
protected_filepath = "../input/geospatial-learn-course-data/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile/SAPA_Aug2019-shapefile-polygons.shp"

# Your code here
protected_areas = gpd.read_file(protected_filepath)

# Check your answer
q_5.check()

# Country boundaries in South America
south_america = americas.loc[americas['continent']=='South America']

# Your code here: plot protected areas in South America
ax = south_america.plot(figsize = (8, 8), color = "whitesmoke", linestyle = ":", edgecolor = "black")
protected_areas.plot(markersize = 1, ax = ax)

# Uncomment to see a hint
q_6.hint()

# Your code here: Calculate the total area of South America (in square kilometers)
totalArea = sum(south_america.geometry.to_crs(epsg = 3035).area) / 10**6

# Check your answer
q_7.check()

# Your code here
ax = south_america.plot(figsize = (8, 8), color = "white", linestyle = ":", edgecolor = "grey")

birds[birds.geometry.y < 0].plot(ax=ax, color='red', alpha=0.6, markersize=10, zorder=2)
protected_areas[protected_areas["MARINE"] != "2"].plot(ax=ax, color='green', markersize=30)

# Uncomment to see a hint
q_8.hint()
