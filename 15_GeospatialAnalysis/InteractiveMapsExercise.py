# Create a base map with plate boundaries
m_1 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)
for i in range(len(plate_boundaries)):
    folium.PolyLine(locations=plate_boundaries.coordinates.iloc[i], weight=2, color='black').add_to(m_1)

# Your code here: Add a heatmap to the map
HeatMap(data = earthquakes[["Latitude", "Longitude"]], radius = 15).add_to(m_1)

# Uncomment to see a hint
q_1.a.hint()

# Show the map
embed_map(m_1, 'q_1.html')

# View the solution (Run this code cell to receive credit!)
# yea, quakes match plate boundaries
q_1.b.solution()

# Create a base map with plate boundaries
m_2 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)
for i in range(len(plate_boundaries)):
    folium.PolyLine(locations=plate_boundaries.coordinates.iloc[i], weight=2, color='black').add_to(m_2)
    
# Your code here: Add a map to visualize earthquake depth
def color_producer(val):
    if val > 100:
        return "forestgreen"
    elif val > 50:
        return "darkred"
    else:
        return "yellow"

from folium import Circle

for i in range(0, len(earthquakes)):
    Circle(
        location = [earthquakes.iloc[i]["Latitude"], earthquakes.iloc[i]["Longitude"]],
        radius = 15,
        color = color_producer(earthquakes.iloc[i]["Depth"])
    ).add_to(m_2)

# Uncomment to see a hint
q_2.a.hint()

# View the map
embed_map(m_2, 'q_2.html')

# View the solution (Run this code cell to receive credit!)
# Depth is smaller as its closer to a plate boundary
q_2.b.solution()

# Create a base map
m_3 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)

from folium import Choropleth

# Your code here: create a choropleth map to visualize population density

plot_dict = stats.density

Choropleth(geo_data=prefectures.__geo_interface__, 
           data=plot_dict, 
           key_on="feature.id", 
           fill_color='YlGnBu', 
           legend_name='Population density'
          ).add_to(m_3)

# Uncomment to see a hint
q_3.a.hint()

# View the map
embed_map(m_3, 'q_3.html')

# View the solution (Run this code cell to receive credit!)
# mainly near tokyo, kanagawa and osaka. that's central japan
q_3.b.solution()

# Create a base map
m_4 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)

# Your code here: create a map

plot_dict = stats.density

Choropleth(geo_data=prefectures["geometry"].__geo_interface__, 
           data=plot_dict, 
           key_on="feature.id", 
           fill_color='YlGnBu', 
           legend_name='Population density'
          ).add_to(m_4)

def color_producer(val):
    if val > 6.5:
        return 'red'
    else:
        return 'green'

# Add a map to visualize earthquake depth
for i in range(0,len(earthquakes)):
    folium.Circle(
        location=[earthquakes.iloc[i]['Latitude'], earthquakes.iloc[i]['Longitude']],
        radius=2000,
        color=color_producer(earthquakes.iloc[i]['Magnitude'])).add_to(m_4)

# Uncomment to see a hint
q_4.a.hint()

# View the map
embed_map(m_4, 'q_4.html')

# View the solution (Run this code cell to receive credit!)
# probably near osaka, and tokyo, but we shouldn't ignore kanagawa tsunami risk
q_4.b.solution()


