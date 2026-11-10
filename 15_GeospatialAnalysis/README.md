<div align="center">

# Geospatial Analysis

**Course 15 of 17 - mapping data, preserving location meaning, joining by geometry, and turning distance into decisions.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Geospatial%20Analysis-20BEFF.svg)](https://www.kaggle.com/learn/geospatial-analysis)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)
![Lessons](https://img.shields.io/badge/Lessons-5%20of%205-brightgreen.svg)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-vector%20data-139C5A.svg)](https://geopandas.org/)
[![Folium](https://img.shields.io/badge/Folium-interactive%20maps-77B829.svg)](https://python-visualization.github.io/folium/)

`PLACE → GEOMETRY → LAYER → PATTERN → DISTANCE → DECISION`

[Course Snapshot](#course-snapshot) · [Mental Model](#the-core-mental-model) · [Lessons](#lesson-tracker) · [First Map](#implemented-first-map) · [CRS](#implemented-coordinate-reference-systems) · [Interactive Maps](#implemented-interactive-maps) · [Manipulation](#implemented-manipulating-geospatial-data) · [Proximity](#implemented-proximity-analysis) · [Skills](#skills-practiced) · [Playbook](#geospatial-analysis-playbook) · [Failure Modes](#common-failure-modes) · [Artifacts](#artifacts) · [Certificate](#certificate-of-completion)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 15 of 17 |
| Estimated time | 4 hours |
| Status | **Complete - 5 of 5 lessons** |
| Started | June 29, 2026 |
| Completed | November 10, 2026 |
| Final lesson | Proximity Analysis |
| Core libraries | GeoPandas, Folium, and geopy's Nominatim geocoder |
| Tasks covered | Loading vector geospatial data, building point geometry from coordinates, assigning and transforming CRS metadata, plotting layered maps, measuring projected area, building interactive heatmaps, styling point markers by attribute, combining choropleth polygons with event overlays, geocoding missing addresses, merging polygon geometry with tabular attributes, filtering candidate regions, spatially joining points to polygons, buffering facility service areas, dissolving buffers into one coverage polygon, isolating uncovered events, routing each event to its nearest facility, ranking facilities by demand, and proposing new sites against a coverage target |
| Running datasets | Kiva loan locations, bird migration tracks, Americas basemap geometry, South American protected areas, Japanese earthquake records, tectonic plate boundaries, Japanese prefecture population density, Berkeley Starbucks stores, California county geometry, county demographic tables, New York City motor-vehicle collisions, and New York City hospital locations |
| Repository artifacts | 5 lesson exports, 1 completion certificate |
| Course page | [Kaggle Learn: Geospatial Analysis](https://www.kaggle.com/learn/geospatial-analysis) |
| Prerequisite context | [Data Visualization](../4_DataVisualization/), [Pandas](../3_Pandas/), and general feature-engineering discipline |

> **Repository truth:** this directory contains all five official lesson exports - [YourFirstMapExercise.py](./YourFirstMapExercise.py), [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py), [InteractiveMapsExercise.py](./InteractiveMapsExercise.py), [ManipulatingGeospatialDataExercise.py](./ManipulatingGeospatialDataExercise.py), and [ProximityAnalysisExercise.py](./ProximityAnalysisExercise.py) - plus the completion certificate. Vector loading, CRS handling, static and interactive layering, geocoding, attribute merges, spatial joins, buffers, coverage unions, nearest-facility distances, and site proposals are all backed by saved work.

## What This Course Adds

Earlier courses treat most rows as independent observations with ordinary scalar features. Geospatial Analysis adds a new type of feature: **place**. A row can now carry geometry - a point, line, or polygon - and that geometry changes what questions are possible.

The first exercise makes the shift concrete. A shapefile is loaded into a `GeoDataFrame`, the geometry column is plotted as point data, and those points are layered over boundary polygons to make the pattern readable. The second exercise adds the rule that makes those maps trustworthy: coordinates only mean something when their coordinate reference system is explicit. The third exercise moves from static figures to exploratory, browser-native maps, where heatmaps, marker styling, choropleths, and layer composition make dense spatial patterns easier to inspect. The fourth exercise starts changing the data itself: missing store coordinates are geocoded from addresses, county polygons are enriched with demographic tables, candidate counties are selected with explicit business rules, and a spatial join counts which stores fall inside the selected polygons. The fifth exercise makes distance itself the feature: hospital service areas are buffered and dissolved into one coverage polygon, collisions outside it are isolated, each is routed to its nearest hospital, and two proposed hospital sites are tested against a citywide coverage target.

The important move is not just drawing a map. It is using location as a first-class analytical object:

- **geometry** stores where each observation is;
- **attributes** store what each observation means;
- **layers** combine multiple spatial datasets in one view;
- **filters** narrow the map to the geography relevant to the question;
- **interactive views** support zooming, panning, and density inspection;
- **spatial operations** - joins, buffers, unions, and distances - answer questions that no shared key can;
- **visual inspection** turns raw coordinates into a spatial hypothesis, and a measured answer turns the hypothesis into a decision.

Each lesson adds one of those moves. Coordinate reference systems keep spatial measurements honest. Interactive maps make dense geography easier to inspect. Spatial joins connect points to containing regions when no ordinary key exists. Proximity analysis turns "near what?" into a model-ready feature or a decision rule. All of them are now backed by saved work.

## The Core Mental Model

```text
Shapefile / GeoJSON / spatial table
              |
              v
        GeoDataFrame
   attributes + geometry column
              |
              v
      Coordinate reference system
   degrees, meters, projection, distance meaning
              |
              v
   Geocode, filter, join, buffer, measure
              |
              v
        Layered map
   basemap + points + polygons + style
              |
              v
 Spatial pattern, service area, coverage gap, or site decision
```

The key habit is to ask whether the operation depends on geometry. Filtering by `country` is ordinary tabular selection. Plotting the result on a country boundary, calculating distance, or asking which features fall within a region is geospatial analysis.

## Lesson Tracker

| # | Lesson | Status | Evidence |
|:-:|--------|:------:|----------|
| 1 | Your First Map | **Complete** | [YourFirstMapExercise.py](./YourFirstMapExercise.py) |
| 2 | Coordinate Reference Systems | **Complete** | [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py) |
| 3 | Interactive Maps | **Complete** | [InteractiveMapsExercise.py](./InteractiveMapsExercise.py) |
| 4 | Manipulating Geospatial Data | **Complete** | [ManipulatingGeospatialDataExercise.py](./ManipulatingGeospatialDataExercise.py) |
| 5 | Proximity Analysis | **Complete** | [ProximityAnalysisExercise.py](./ProximityAnalysisExercise.py) |

### Course trajectory

```text
Load vector data
      ↓
Layer points on polygons
      ↓
Respect coordinate reference systems
      ↓
Inspect geography interactively
      ↓
Geocode, enrich, and spatially join
      ↓
Buffer, measure distance, and decide where to build
```

## Implemented First Map

The saved exercise completes the first geospatial workflow: load Kiva loan locations, plot them globally, filter to one country, and interpret the country-level spatial pattern.

### 1. Load vector data into a GeoDataFrame

```python
loans_filepath = "../input/geospatial-learn-course-data/kiva_loans/kiva_loans/kiva_loans.shp"
world_loans = gpd.read_file(loans_filepath)
```

`gpd.read_file` reads the shapefile and returns a `GeoDataFrame`. It behaves like a pandas DataFrame with one extra responsibility: a geometry column that stores spatial objects. In this lesson, each Kiva loan has point geometry, so plotting the GeoDataFrame draws loan locations.

### 2. Plot points over a polygon basemap

```python
ax = world.plot(
    figsize=(20, 20),
    color="whitesmoke",
    linestyle=":",
    edgecolor="black",
)
world_loans.plot(ax=ax, markersize=2)
```

The map uses two layers:

- `world` supplies country polygons, drawn first as context.
- `world_loans` supplies point geometry, drawn second on the same axes.

Layer order matters. If points are drawn before the basemap, the polygons can cover them. Drawing the basemap first and passing its axes into the point layer keeps the loan locations visible while preserving geographic context.

### 3. Filter spatial data with tabular logic

```python
PHL_loans = world_loans.loc[world_loans.country.isin(["Philippines"])]
```

This is ordinary pandas-style filtering applied to a GeoDataFrame. The geometry stays attached to each selected row, so the filtered result remains spatial data and can be plotted directly.

### 4. Re-plot at the country scale

```python
ax = PHL.plot(
    figsize=(20, 20),
    color="whitesmoke",
    linestyle=":",
    edgecolor="black",
)
PHL_loans.plot(ax=ax, markersize=2)
```

The second map switches from the world basemap to the Philippines basemap. That makes local concentration easier to see because the relevant geography uses the full plotting area instead of being compressed into a global view.

### 5. Interpret the spatial pattern

The saved answer identifies noticeable concentrations around northern Mindanao, Cagayan Valley, and parts of Western and Central Visayas. This is the analytical finish line for the first lesson: the code produces a map, but the work is not complete until the map is read as evidence.

## Implemented Coordinate Reference Systems

The second saved exercise moves from "plot the geometry" to "know what the coordinates mean." It builds point geometry from latitude and longitude, assigns the coordinate reference system, transforms geometry for plotting or measurement, derives migration endpoints, overlays paths and protected areas, and calculates area only after moving into a projected CRS.

### 1. Build point geometry from longitude and latitude

```python
birds = gpd.GeoDataFrame(
    birds_df,
    geometry=gpd.points_from_xy(
        birds_df["location-long"],
        birds_df["location-lat"],
    ),
)
birds.crs = {"init": "epsg:4326"}
```

The raw bird records start as ordinary tabular data with separate longitude and latitude columns. `gpd.points_from_xy` turns those scalar columns into Shapely point geometry, and `GeoDataFrame` keeps the original bird attributes attached to each point. Setting the CRS to EPSG:4326 records that the coordinates are geographic latitude/longitude values.

### 2. Reproject before combining map layers

```python
ax = americas.plot(
    figsize=(8, 8),
    color="whitesmoke",
    linestyle=":",
    edgecolor="black",
)
birds.to_crs(epsg=4326).plot(markersize=1, ax=ax)
```

CRS alignment is a precondition for meaningful layering. Even when two datasets look similar, the map is only trustworthy if both layers use the same coordinate system before they are drawn together. In this exercise the target is EPSG:4326; the general habit is to pick an explicit target CRS and align every plotted layer to it.

### 3. Derive end locations by bird identifier

```python
end_df = (
    birds.groupby("tag-local-identifier")["geometry"]
    .apply(list)
    .apply(lambda x: x[-1])
    .reset_index()
)
end_gdf = gpd.GeoDataFrame(end_df, geometry=end_df.geometry)
end_gdf.crs = {"init": "epsg:4326"}
```

The exercise keeps the data-model split clean: grouping and choosing each bird's final observation is tabular logic, while wrapping the result back into a `GeoDataFrame` preserves the spatial meaning needed for plotting.

### 4. Layer starts, paths, and endpoints

```python
ax = americas.plot(figsize=(8, 8), color="white", linestyle=":", edgecolor="grey")

start_gdf.plot(ax=ax, color="red", markersize=30)
path_gdf.plot(ax=ax, cmap="tab20b", linestyle="-", linewidth=1, zorder=1)
end_gdf.plot(ax=ax, color="black", markersize=30)
```

The migration map uses visual roles rather than one undifferentiated point cloud: starts are red, movement paths are colored lines, and endpoints are black. That makes the map answer a sequence question: where did each bird begin, how did it move, and where did it finish?

### 5. Measure area in a projected CRS

```python
totalArea = sum(south_america.geometry.to_crs(epsg=3035).area) / 10**6
```

Area is not measured honestly in latitude/longitude degrees. The exercise converts South American polygons to EPSG:3035 before reading `.area`, then divides by `10**6` to convert square meters to square kilometers. The important lesson is the unit change: project geometry before measuring area. For production analysis, the projection should also be chosen for the geography being measured, not copied blindly from an exercise check.

### 6. Compare migration points with protected areas

```python
birds[birds.geometry.y < 0].plot(ax=ax, color="red", alpha=0.6, markersize=10, zorder=2)
protected_areas[protected_areas["MARINE"] != "2"].plot(ax=ax, color="green", markersize=30)
```

The final map filters bird observations to the Southern Hemisphere and filters protected areas to non-marine records. The resulting overlay asks a spatial coverage question: do the observed migration locations appear near protected land areas?

## Implemented Interactive Maps

The third saved exercise switches from static matplotlib maps to Folium maps rendered as HTML. The running geography is Japan: earthquake records, tectonic plate boundaries, and prefecture-level population density. The lesson's core upgrade is interaction. Zooming and panning make dense geographic evidence easier to inspect, while Folium layers let the same map answer several spatial questions at once.

### 1. Build a reusable base map

```python
m_1 = folium.Map(location=[35, 136], tiles="cartodbpositron", zoom_start=5)
for i in range(len(plate_boundaries)):
    folium.PolyLine(
        locations=plate_boundaries.coordinates.iloc[i],
        weight=2,
        color="black",
    ).add_to(m_1)
```

The base map centers Japan, uses a subdued tile layer, and draws tectonic plate boundaries as black polylines. That keeps the physical geography visible without competing with the earthquake overlays added later.

### 2. Use a heatmap for earthquake concentration

```python
HeatMap(data=earthquakes[["Latitude", "Longitude"]], radius=15).add_to(m_1)
```

The heatmap converts many individual earthquake coordinates into a density surface. The saved interpretation records that the earthquake clusters align with plate boundaries, which is the first useful spatial claim: event concentration is not random across the map.

### 3. Style point markers by earthquake depth

```python
def color_producer(val):
    if val > 100:
        return "forestgreen"
    elif val > 50:
        return "darkred"
    else:
        return "yellow"

for i in range(0, len(earthquakes)):
    Circle(
        location=[earthquakes.iloc[i]["Latitude"], earthquakes.iloc[i]["Longitude"]],
        radius=15,
        color=color_producer(earthquakes.iloc[i]["Depth"]),
    ).add_to(m_2)
```

This map keeps the same tectonic context but changes the question from "where are earthquakes dense?" to "how does depth vary across those locations?" Depth becomes visual state through marker color, and the written answer notes the pattern that shallower events appear closer to plate boundaries.

### 4. Create a population-density choropleth

```python
Choropleth(
    geo_data=prefectures.__geo_interface__,
    data=stats.density,
    key_on="feature.id",
    fill_color="YlGnBu",
    legend_name="Population density",
).add_to(m_3)
```

The choropleth turns prefecture polygons into a regional population-density layer. The saved interpretation identifies the strongest density around Tokyo, Kanagawa, Osaka, and central Japan. That is a different kind of spatial evidence than point events: the geometry is now administrative regions colored by an attribute.

### 5. Combine exposure and hazard layers

```python
Choropleth(
    geo_data=prefectures["geometry"].__geo_interface__,
    data=stats.density,
    key_on="feature.id",
    fill_color="YlGnBu",
    legend_name="Population density",
).add_to(m_4)

for i in range(0, len(earthquakes)):
    folium.Circle(
        location=[earthquakes.iloc[i]["Latitude"], earthquakes.iloc[i]["Longitude"]],
        radius=2000,
        color=color_producer(earthquakes.iloc[i]["Magnitude"]),
    ).add_to(m_4)
```

The final interactive map layers population density with earthquake magnitude markers. That turns the map into an exposure screen: high-density prefectures and strong earthquake locations can be inspected together. The saved conclusion flags Osaka and Tokyo as likely concerns while keeping Kanagawa in view for tsunami-risk reasoning.

## Implemented Manipulating Geospatial Data

The fourth saved exercise turns mapped records into decision-ready spatial data. The running question is where Starbucks might expand in California. The workflow repairs missing store coordinates, maps known Berkeley stores, enriches county polygons with demographic tables, filters counties by business criteria, and uses a spatial join to count existing stores inside the selected regions.

### 1. Geocode missing coordinates from addresses

```python
geolocator = Nominatim(user_agent="kaggle_learn")

def my_geocoder(row):
    point = geolocator.geocode(row).point
    return pd.Series({"Latitude": point.latitude, "Longitude": point.longitude})

berkeley_locations = rows_with_missing.apply(lambda x: my_geocoder(x["Address"]), axis=1)
starbucks.update(berkeley_locations)
```

The exercise starts with incomplete point data. `Nominatim` converts address strings into latitude/longitude coordinates, and the helper returns a two-column `Series` so the result can be aligned back to the original table. `starbucks.update(...)` then fills the missing coordinate fields without rebuilding the whole DataFrame.

### 2. Inspect repaired locations on an interactive map

```python
m_2 = folium.Map(location=[37.88, -122.26], zoom_start=13)

for idx, row in starbucks[starbucks["City"] == "Berkeley"].iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup=row["Store Name"]).add_to(m_2)
```

After geocoding, the map becomes the sanity check. Each Berkeley store is added as a Folium marker with the store name as popup text. This verifies that the repaired coordinates land in the expected city before those records are trusted in later analysis.

### 3. Enrich county polygons with tabular attributes

```python
CA_stats = CA_counties.merge(CA_pop, on="GEOID")
CA_stats = CA_stats.merge(CA_high_earners, on="GEOID")
CA_stats = CA_stats.merge(CA_median_age, on="GEOID")
```

County geometry alone can draw a map, but it cannot answer the expansion question. The saved workflow joins population density, high-earner counts, and median age onto the county polygons through the shared `GEOID` key. The result is still spatial data because the county geometry remains attached after the merges.

### 4. Filter candidate counties with explicit criteria

```python
sel_counties = CA_stats[
    ((CA_stats.high_earners > 100000) &
     (CA_stats.median_age < 38.5) &
     (CA_stats.density > 285) &
     ((CA_stats.median_age < 35.5) |
      (CA_stats.density > 1400) |
      (CA_stats.high_earners > 500000)))
]
```

The county filter is deliberately transparent: every retained county must meet the baseline demographic thresholds, then satisfy at least one stronger signal. This is not a model yet; it is a readable site-screening rule that can be debated, tuned, or replaced.

### 5. Count stores inside selected polygons

```python
num_stores = len(gpd.sjoin(starbucks_gdf, sel_counties))
```

This is the lesson's central geospatial operation. There is no ordinary table key saying which county contains each Starbucks point. `gpd.sjoin` derives that relationship from geometry, attaching point records to polygons by spatial relationship and making a point-in-polygon count possible.

### 6. Map selected stores for review

```python
m_6 = folium.Map(location=[37, -120], zoom_start=6)

for idx, row in gpd.sjoin(starbucks_gdf, sel_counties).iterrows():
    Marker([row["Latitude"], row["Longitude"]], popup=row["Store Name"]).add_to(m_6)
```

The final map displays stores that fall inside the selected counties. This closes the loop: the attribute filter identifies promising regions, the spatial join finds stores located inside them, and the Folium review map makes the result inspectable before treating it as a decision.

## Implemented Proximity Analysis

The fifth saved exercise closes the course with a public-health siting problem in New York City. Two datasets share the EPSG:2263 coordinate reference system: major motor-vehicle collisions from 2013 to 2018 and the city's hospitals. The question is operational rather than descriptive: which crashes happen too far from any hospital, which hospital would absorb them, and where should two new hospitals go so that fewer than ten percent of collisions remain outside the course's 10 km service radius?

### 1. Map collision density

```python
m_1 = folium.Map(location=[40.7, -74], zoom_start=11)

HeatMap(data=collisions[["LATITUDE", "LONGITUDE"]], radius=15).add_to(m_1)
for idx, row in collisions.iterrows():
    Marker([row["LATITUDE"], row["LONGITUDE"]]).add_to(m_1)
```

The exercise opens by asking which map type is most effective for the collision data. The saved answer uses both candidates at once: a `HeatMap` summarizes where crashes concentrate, and a `Marker` per record keeps individual incidents inspectable at street zoom. The heatmap carries the analytical signal; the markers are the audit trail.

### 2. Map hospital locations

```python
m_2 = folium.Map(location=[40.7, -74], zoom_start=11)

HeatMap(data=hospitals[["latitude", "longitude"]], radius=15).add_to(m_2)
for idx, row in hospitals.iterrows():
    Marker([row["latitude"], row["longitude"]]).add_to(m_2)
```

The same recipe is applied to the supply side. Drawing both layers at the same center and zoom is what makes the gap visible: dense crash corridors in the outer boroughs with no hospital marker nearby.

### 3. Isolate collisions outside hospital coverage

```python
coverage = gpd.GeoDataFrame(geometry=hospitals.geometry).buffer(10000)
my_union = coverage.geometry.unary_union
outside_range = collisions.loc[~collisions["geometry"].apply(lambda x: my_union.contains(x))]
```

This is the lesson's central construction. `buffer(10000)` draws a service-area polygon around every hospital in the CRS's linear units, which the course treats as 10 kilometers. `unary_union` dissolves the overlapping circles into one coverage multipolygon, so the containment test is asked once per collision instead of once per hospital. `contains` then flags covered crashes, and the `~` negation keeps the ones that no service area reaches. The archived file keeps the first, loop-based attempt commented above the vectorized version - a record of the shift from "check each hospital for each crash" to "build the coverage once, then filter."

### 4. Route any collision to its nearest hospital

```python
def best_hospital(collision_location):
    distances = hospitals.geometry.distance(collision_location)
    name = hospitals.iloc[distances.idxmin()]["name"]
    return name

print(best_hospital(outside_range.geometry.iloc[0]))  # CALVARY HOSPITAL INC
```

`GeoSeries.distance` measures from one collision point to every hospital in a single vectorized call, and `idxmin` returns the index label of the closest one. Because `hospitals` carries its default integer index, `iloc` on that label resolves the row and its `name`. The exercise's own test case - the first out-of-range crash should resolve to Calvary Hospital - is preserved in the saved file.

### 5. Find the hospital under the most pressure

```python
highest_demand = outside_range.geometry.apply(best_hospital).value_counts().idxmax()
```

Applying the nearest-hospital function to every out-of-range collision produces one hospital name per crash. `value_counts` tallies them and `idxmax` returns the most frequent: in the saved work, Jamaica Hospital Medical Center. The commented-out dictionary loop above it is the same computation written by hand before being collapsed into one pandas chain.

### 6. Propose two new hospital sites

```python
lat_1 = 40.6598
long_1 = -73.7567

lat_2 = 40.6702
long_2 = -73.8611
```

Both proposed sites sit in southern Queens, where the out-of-range collisions concentrate: one beside JFK Airport, the other near the Brooklyn-Queens border around Ozone Park. The course's check cell then runs the honest version of the test. The points are built in EPSG:4326 with `points_from_xy`, reprojected to EPSG:2263 so the new buffers use the same units as the existing coverage, dissolved with `unary_union`, and used to recompute the share of all collisions still outside any service area against the target of less than ten percent.

```python
folium.GeoJson(coverage.geometry.to_crs(epsg=4326)).add_to(m)
folium.GeoJson(new_coverage.geometry.to_crs(epsg=4326)).add_to(m)
for idx, row in new_gdf.iterrows():
    Marker([row["Latitude"], row["Longitude"]]).add_to(m)
HeatMap(data=new_outside_range[["LATITUDE", "LONGITUDE"]], radius=9).add_to(m)
folium.LatLngPopup().add_to(m)
```

The review map introduces two Folium tools the earlier lessons did not need. `GeoJson` draws the existing and proposed coverage polygons after reprojecting them back to latitude/longitude for the web map, and `LatLngPopup` prints the coordinates of any clicked point, which is how the exercise invites you to pick candidate sites. The remaining uncovered crashes are drawn as a tighter heatmap so the residual gap is visible at a glance.

## Skills Practiced

From the five solved exercises:

- Loading shapefile data with `gpd.read_file`
- Treating a `GeoDataFrame` as a DataFrame plus geometry
- Inspecting loaded spatial records with `.head()`
- Creating point geometry from longitude and latitude with `gpd.points_from_xy`
- Geocoding missing latitude/longitude fields from address strings with `Nominatim`
- Returning geocoded latitude and longitude as a `pd.Series`
- Updating existing coordinate columns with `DataFrame.update`
- Assigning CRS metadata with `.crs`
- Transforming geometry with `.to_crs(...)`
- Plotting country boundary polygons with GeoPandas
- Plotting point geometries on top of an existing matplotlib axis
- Plotting line/path geometries alongside points and polygons
- Controlling map context with `figsize`, `color`, `linestyle`, and `edgecolor`
- Keeping layer order deliberate so basemap polygons do not hide point data
- Filtering geospatial records with `.loc`
- Selecting country-specific rows with `.isin(["Philippines"])`
- Filtering point geometries with coordinate accessors such as `geometry.y`
- Filtering polygon attributes such as `MARINE`
- Grouping spatial records by identifier to derive endpoint geometry
- Re-wrapping grouped geometry results as a `GeoDataFrame`
- Calculating polygon area only after projecting to a CRS with useful linear units
- Converting square meters to square kilometers
- Reusing the same plotting pattern at global and national scales
- Creating interactive Folium maps with `folium.Map`
- Choosing tile style and zoom level to make the analytical layer readable
- Drawing line geometry with `folium.PolyLine`
- Drawing location markers with `folium.Marker`
- Adding popup labels to interactive point markers
- Adding point-density heatmaps with `HeatMap`
- Encoding numeric attributes into marker color with a helper function
- Drawing interactive point overlays with `folium.Circle`
- Creating polygon choropleths with `folium.Choropleth`
- Passing GeoPandas geometry into Folium with `__geo_interface__`
- Connecting choropleth data to geometry with `key_on="feature.id"`
- Combining density polygons and event markers in one interactive view
- Merging polygon geometry with tabular demographic tables on `GEOID`
- Building compound boolean filters over demographic attributes
- Using `gpd.sjoin` to connect point records with containing polygon regions
- Counting point-in-polygon matches with `len(...)`
- Building facility service areas with `GeoSeries.buffer`
- Dissolving overlapping buffers into one coverage geometry with `unary_union`
- Testing point containment against a multipolygon with `contains`
- Negating a boolean selection with `~` to keep uncovered events
- Measuring point-to-facility distances with `GeoSeries.distance`
- Selecting the nearest facility with `idxmin`
- Wrapping nearest-facility lookup in a reusable function
- Ranking facility demand with `apply`, `value_counts`, and `idxmax`
- Proposing candidate coordinates and validating them in the projected CRS
- Drawing polygon layers in Folium with `folium.GeoJson`
- Reading coordinates interactively with `folium.LatLngPopup`
- Reprojecting projected geometry back to EPSG:4326 for web-map display
- Keeping a first draft commented beside the vectorized final answer
- Exporting notebook maps to HTML with `embed_map`
- Separating data loading, filtering, visualization, and interpretation into distinct steps
- Reading spatial concentration as evidence rather than treating the map as decoration
- Preserving Kaggle answer checks alongside solved notebook cells

## Why Each Choice Matters

| Choice | Role | If it is wrong |
|--------|------|----------------|
| `gpd.read_file` | Loads vector geometry and attributes together | Location columns may be lost or treated as plain text |
| `gpd.points_from_xy` | Converts longitude and latitude columns into point geometry | Coordinates stay as ordinary numbers and cannot be plotted or spatially transformed as geometry |
| `.crs` assignment | Records what coordinate values mean | Later overlays, transformations, and measurements can silently become invalid |
| `.to_crs(...)` | Reprojects geometry into a target coordinate system | Layers can be misaligned or measurements can use meaningless units |
| Shapefile input | Provides points, metadata, and spatial reference as a dataset bundle | Missing companion files can make the read fail or strip spatial meaning |
| Polygon basemap | Gives the point layer geographic context | Points appear as an unanchored cloud |
| Shared matplotlib axis | Places multiple GeoDataFrames in one map | Each layer appears in a separate figure instead of one composition |
| Basemap first, points second | Keeps observations visible above the background | Polygons can cover the data being analyzed |
| Small point marker size | Makes dense global data readable | Large markers can hide clustering and overlap |
| Distinct start/path/end styling | Separates the stages of movement | Migration structure collapses into an unreadable pile of marks |
| Country filter | Narrows the analysis to the question's geography | Global scale can hide the local pattern |
| Country-specific basemap | Gives the filtered points useful local context | The viewer must infer boundaries and regions mentally |
| Projected area calculation | Uses linear units before computing square units | `.area` on degree coordinates produces numbers that look precise but are not useful area measurements |
| `folium.Map` | Creates an interactive browser map with zoom, pan, and tile context | Dense geography is harder to inspect from one fixed static view |
| `HeatMap` | Converts many event points into a density surface | Overlapping points can hide the strongest concentration zones |
| `folium.Circle` styling | Encodes event attributes such as depth or magnitude on individual locations | Important differences between events disappear into one uniform marker layer |
| `Choropleth` | Colors polygon regions by an attached numeric attribute | Regional exposure patterns stay trapped in a table |
| Combined hazard/exposure layers | Puts event severity and population density in the same decision view | Risk reasoning has to happen across separate maps by memory |
| Address geocoding | Recovers usable coordinates when a record only has a street address | The row cannot participate in point mapping or spatial joins |
| `DataFrame.update` | Fills corrected coordinate values while preserving the rest of the table | Repaired coordinates can become detached from the original store records |
| `GEOID` merges | Attaches demographic attributes to county polygons through a stable administrative key | County geometry and demographic facts can be mismatched |
| Compound county filter | Makes the site-selection rule explicit and auditable | Candidate regions are selected by hidden judgment instead of reviewable criteria |
| `gpd.sjoin` | Derives point-in-polygon relationships from geometry | Store counts by selected county cannot be computed from location alone |
| `GeoSeries.buffer(10000)` | Turns each facility point into a service-area polygon in projected units | Buffering in degrees produces shapes of meaningless size; buffering in the wrong linear unit shifts the whole threshold |
| `unary_union` | Dissolves overlapping buffers into one coverage geometry | Overlaps are double-counted and every point must be tested against every buffer |
| `~ ... contains` filter | Keeps only the events that no service area reaches | The analysis reports covered crashes instead of the gap it is meant to find |
| `distance` + `idxmin` | Resolves the nearest facility in one vectorized call | Hand-written loops are slower and easier to get wrong at index boundaries |
| `value_counts().idxmax()` | Converts per-event routing into a facility-level demand ranking | The busiest receiving hospital stays hidden in a list of names |
| Reprojecting proposals to EPSG:2263 | Tests new sites in the same units as the existing coverage | New buffers are drawn in degrees and the coverage percentage is fiction |
| `folium.GeoJson` | Draws coverage polygons on the interactive review map | Service areas can only be reasoned about numerically, never seen |
| `folium.LatLngPopup` | Reads coordinates straight off the map | Candidate sites have to be looked up elsewhere and transcribed |
| Written interpretation | Converts a visualization into an analytical claim | The work stops at plotting instead of analysis |

## Geospatial Analysis Playbook

This is the workflow the course builds. The five exercises walk it end to end, from loading a shapefile to proposing where a city should build.

1. **Identify the spatial unit.** Know whether each row is a point, line, polygon, grid cell, address, or administrative region.
2. **Load geometry and attributes together.** Prefer spatial readers such as `gpd.read_file` when a file already encodes geometry.
3. **Inspect before plotting.** Check columns, geometry type, row count, missing values, and coordinate reference system.
4. **Choose the right map scale.** A global plot is useful for context; a regional plot is better for local patterns.
5. **Layer deliberately.** Draw context first, then observations, then highlights or annotations.
6. **Preserve CRS meaning.** Assign the source CRS, align layers before plotting, and do not measure distance or area until the CRS makes those units valid.
7. **Use interactive maps for dense inspection.** Heatmaps, choropleths, and styled markers help when static plots hide overlap or local detail.
8. **Use spatial operations when the question is spatial.** Buffers, joins, overlays, and distances should answer geography-driven questions, not replace simple tabular filters.
9. **Measure in projected units, and confirm which units.** Buffer, distance, and area need a CRS with linear units, and the registry contains both meters and feet - read `crs.axis_info` before trusting a threshold.
10. **Dissolve before you test.** Merge overlapping service areas into one geometry so each event is checked once against the whole coverage, not once per facility.
11. **Quantify coverage, not just draw it.** A service-area map is a picture; the share of events outside it is a metric that can be targeted, re-tested, and reported.
12. **Interpret the map and record assumptions.** State the visible pattern, the uncertainty, the decision it supports, and the projection, filters, data vintage, and simplifications that could change the result.

## GeoDataFrame Reference

| Concept | Meaning |
|---------|---------|
| Attribute columns | Ordinary tabular fields such as country, amount, category, or date |
| Geometry column | Spatial object attached to each row, usually points, lines, or polygons |
| Geographic CRS | Coordinate reference system using angular units such as latitude and longitude |
| Projected CRS | Coordinate reference system using planar units such as meters, suitable for many distance or area operations |
| CRS transform | Geometry conversion from one coordinate reference system to another |
| Layer | One plotted spatial dataset in a map composition |
| Basemap | Context layer used to orient the main analytical layer |
| Geocoding | Converting an address or place name into latitude and longitude |
| Heatmap | Interactive density layer that summarizes where many point events concentrate |
| Choropleth | Polygon map that colors regions by an attribute value |
| Marker styling | Visual encoding of point attributes through color, radius, opacity, or icon state |
| Point-in-polygon | Test that determines whether point geometry falls inside polygon geometry |
| Spatial filter | Selection based on location, intersection, containment, or distance |
| Spatial join | Attribute merge driven by geometry relationships instead of a shared key |
| Buffer | New geometry representing a fixed distance around existing geometry |
| Union (dissolve) | Single geometry formed by merging overlapping shapes, so coverage can be tested once |
| Service area | Buffer around a facility representing the region it can reasonably reach |
| Coverage gap | Events or places that fall outside every service area |
| Nearest facility | The facility at minimum distance from a given point, found with `distance` and `idxmin` |
| Projected units | Linear units - meters or feet - attached to a projected CRS; the only safe basis for buffers and distances |

## Common Failure Modes

| Symptom | Likely cause | Check first |
|---------|--------------|-------------|
| Points land in the ocean or on the wrong continent | Latitude and longitude passed in the wrong order | `points_from_xy(x=longitude, y=latitude)`; Folium wants `[lat, lon]` |
| Layers do not line up on the same map | Mismatched coordinate reference systems | Compare `.crs` on every layer and align with `to_crs` before plotting |
| Area or distance values are tiny or absurd | Geometry measured in degrees | Reproject to a projected CRS before calling `.area`, `.distance`, or `.buffer` |
| Buffers are the right shape but the wrong size | The CRS's linear unit is not what was assumed | Read `gdf.crs.axis_info` and confirm meters versus US survey feet |
| Spatial join returns zero rows or far too many | CRS mismatch, or the wrong spatial predicate | Align CRSs, then set `predicate="within"` or `"intersects"` explicitly |
| Choropleth renders with no fill | `key_on` does not match the ids in the GeoJSON | Inspect `__geo_interface__` feature ids against the data index |
| Heatmap looks like one uniform blob | `radius` too large for the zoom level | Lower `radius` or raise `zoom_start` |
| Geocoder raises or returns `None` | Ambiguous address, rate limit, or no match | Handle `None`, cache results, and respect the Nominatim usage policy |
| Nearest-facility lookup returns the wrong row | `idxmin` label used as a position after the index was filtered or reordered | Use `.loc` with the label, or `argmin` with `.iloc` |
| Folium map shows nothing in the notebook | Layers added to a different map object, or the map was never displayed | Check which `m_*` each `.add_to` targets and call `embed_map` on that one |

## Artifacts

- [YourFirstMapExercise.py](./YourFirstMapExercise.py) - loads Kiva loan shapefile data, plots loan points over a world basemap, filters loans in the Philippines, plots them over a Philippines basemap, and records a regional concentration reading.
- [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py) - creates bird-location point geometry from longitude/latitude columns, assigns EPSG:4326 CRS metadata, plots migration starts, paths, and endpoints, loads protected-area polygons, reprojects South America before area calculation, and overlays Southern Hemisphere bird observations with non-marine protected areas.
- [InteractiveMapsExercise.py](./InteractiveMapsExercise.py) - builds Folium maps for Japanese earthquake analysis, including plate-boundary polylines, earthquake heatmaps, depth-colored point markers, prefecture population-density choropleths, and a combined population-density plus earthquake-magnitude exposure view.
- [ManipulatingGeospatialDataExercise.py](./ManipulatingGeospatialDataExercise.py) - geocodes missing Berkeley Starbucks coordinates, maps repaired store locations, merges California county geometry with demographic tables, filters candidate counties, spatially joins Starbucks points to the selected county polygons, and maps the selected stores.
- [ProximityAnalysisExercise.py](./ProximityAnalysisExercise.py) - maps New York City collisions and hospitals with heatmaps and markers, buffers hospitals into 10,000-unit service areas, dissolves them with `unary_union`, isolates collisions outside coverage, resolves the nearest hospital for any collision with `distance` and `idxmin`, ranks hospitals by out-of-range demand, and proposes two new hospital sites validated against the course's coverage target.
- [Cux Prada - Geospatial Analysis.png](./Cux%20Prada%20-%20Geospatial%20Analysis.png) - completion certificate, dated November 10, 2026.

## Course Notes

- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, preloaded objects such as `world`, `PHL`, `americas`, `start_gdf`, `path_gdf`, `plate_boundaries`, `prefectures`, `stats`, `rows_with_missing`, `starbucks`, `CA_counties`, `CA_pop`, `CA_high_earners`, `CA_median_age`, `starbucks_gdf`, `collisions`, and `hospitals`, GeoPandas/Folium setup, plotting context, HTML embedding helpers, and answer-checking helpers such as `q_1.check()`.
- The CRS exercise uses the course's `{"init": "epsg:4326"}` style because that is what the notebook prompt expects. In modern GeoPandas code, `set_crs(epsg=4326)` is usually clearer when assigning a CRS to geometry that already has coordinates but lacks metadata.
- The first lesson uses vector data. The shapes are not pixels; they are geometric objects with attributes.
- The map is analytical because each plotted point is tied back to a row in `world_loans`.
- The same object can be filtered like pandas data and plotted like spatial data, which is the practical value of GeoPandas.
- The second lesson makes coordinate reference systems explicit before serious distance or area reasoning. EPSG:4326 is useful for storing and plotting latitude/longitude positions, but projected CRSs are required when the numeric units need to represent meters or square meters.
- The protected-area overlay is a visual coverage check, not a formal spatial operation. The fifth lesson replaces visual proximity with explicit buffers, unions, and distances.
- The third lesson makes browser maps useful for analysis rather than presentation alone: heatmaps summarize event density, choropleths summarize regional exposure, and marker styling keeps individual event attributes visible.
- Folium maps are saved through Kaggle's `embed_map(...)` helper in the notebook environment. The exported Python file records those calls, but the generated `q_*.html` map files are not stored in this repository.
- The fourth lesson introduces geocoding through the public `Nominatim` service. In production work, geocoded results should be cached, requests should respect service rate limits, and missing or ambiguous address matches should be handled explicitly.
- The saved `gpd.sjoin(starbucks_gdf, sel_counties)` calls rely on the Kaggle notebook's GeoPandas behavior for the spatial predicate. In production code, the predicate should be set explicitly when the distinction between `intersects`, `within`, and `contains` matters.
- The Starbucks county filter is a transparent exercise rule, not a validated expansion model. Its value here is that the spatial data path is auditable: enrich polygons, filter regions, join points, then inspect the map.
- The fifth lesson's exercise text states that EPSG:2263 has units of meters and frames `buffer(10000)` as a 10 km service radius. The EPSG registry defines 2263 (NAD83 / New York Long Island) in US survey feet, so the same number is a materially shorter radius if the data really is in that projection. The saved answer follows the course convention because that is what the checker expects; in real work, read `gdf.crs.axis_info` before choosing a buffer distance.
- `unary_union` is the attribute the course teaches. GeoPandas 1.0 deprecates it in favor of `union_all()`, which performs the same dissolve.
- `best_hospital` indexes with `iloc` on the label returned by `idxmin`. That is only safe because `hospitals` keeps its default integer index; after any filtering or sorting, use `.loc` with the label or `argmin` with `.iloc`.
- The course's completion check reprojects the proposed sites to EPSG:2263 before buffering. That is the correct order: build geometry in the CRS the coordinates were read in, then transform into the CRS whose units the measurement needs.
- The commented-out loops in [ProximityAnalysisExercise.py](./ProximityAnalysisExercise.py) are kept on purpose. They record the first working approach beside the vectorized one that replaced it.

## Completion Standard

The course completion standard is satisfied: all five official exercise exports and the certificate are present.

- [x] Your First Map
- [x] Coordinate Reference Systems
- [x] Interactive Maps
- [x] Manipulating Geospatial Data
- [x] Proximity Analysis
- [x] Completion certificate archived
- [x] Root roadmap updated from 14/17 to 15/17

## Takeaway

The five lessons establish one idea at two levels: **location is a feature, and geometry is how it is computed on.** A `GeoDataFrame` keeps attributes and geometry together; the coordinate reference system says what the geometry's numbers mean; layered static and interactive maps turn coordinates into visible pattern; geocoding, merges, and spatial joins attach meaning to places that share no ordinary key; and buffers, unions, and distances turn "near what?" into a number that a decision can be tested against.

The engineering discipline matters as much as the operations: assign the CRS before anything else, align layers before drawing them together, project before measuring, confirm the projected unit, dissolve before testing containment, keep index labels and positions straight, and finish every map with a written claim about what it shows and what it leaves uncertain.

## Certificate of Completion

<div align="center">

<a href="./Cux%20Prada%20-%20Geospatial%20Analysis.png"><img src="./Cux%20Prada%20-%20Geospatial%20Analysis.png" width="600" alt="Geospatial Analysis certificate" /></a>

*Completed November 10, 2026.*

</div>

---

<div align="center">

[← Computer Vision](../14_ComputerVision/) · [Back to Roadmap](../README.md) · [Intro to Game AI and Reinforcement Learning →](https://www.kaggle.com/learn/intro-to-game-ai-and-reinforcement-learning)

</div>
