<div align="center">

# Geospatial Analysis

**Course 15 of 17 - mapping data, preserving location meaning, and turning geometry into analytical evidence.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Geospatial%20Analysis-20BEFF.svg)](https://www.kaggle.com/learn/geospatial-analysis)
![Status](https://img.shields.io/badge/Status-In%20Progress-f5b642.svg)
![Lessons](https://img.shields.io/badge/Lessons-2%20of%205-f5b642.svg)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-ready-139C5A.svg)](https://geopandas.org/)

`PLACE -> GEOMETRY -> LAYER -> PATTERN -> DECISION`

[Course Snapshot](#course-snapshot) . [Mental Model](#the-core-mental-model) . [Lessons](#lesson-tracker) . [First Map](#implemented-first-map) . [CRS](#implemented-coordinate-reference-systems) . [Skills](#skills-practiced) . [Playbook](#geospatial-analysis-playbook) . [Artifacts](#artifacts)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 15 of 17 |
| Estimated time | 4 hours |
| Status | **In progress - 2 of 5 lessons archived** |
| Started | June 29, 2026 |
| Latest archived lesson | Coordinate Reference Systems |
| Core library | GeoPandas |
| Tasks covered | Loading vector geospatial data, building point geometry from coordinates, assigning and transforming CRS metadata, plotting layered maps, and measuring projected area |
| Running dataset | Kiva loan locations, bird migration tracks, Americas basemap geometry, and South American protected areas |
| Repository artifacts | 2 lesson exports |
| Course page | [Kaggle Learn: Geospatial Analysis](https://www.kaggle.com/learn/geospatial-analysis) |
| Prerequisite context | [Data Visualization](../4_DataVisualization/), [Pandas](../3_Pandas/), and general feature-engineering discipline |

> **Repository truth:** this directory currently contains the first two official lesson exports: [YourFirstMapExercise.py](./YourFirstMapExercise.py) and [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py). The remaining three course lessons are tracked below but are not backed by saved local work yet.

## What This Course Adds

Earlier courses treat most rows as independent observations with ordinary scalar features. Geospatial Analysis adds a new type of feature: **place**. A row can now carry geometry - a point, line, or polygon - and that geometry changes what questions are possible.

The first exercise makes the shift concrete. A shapefile is loaded into a `GeoDataFrame`, the geometry column is plotted as point data, and those points are layered over boundary polygons to make the pattern readable. The second exercise adds the rule that makes those maps trustworthy: coordinates only mean something when their coordinate reference system is explicit. The important move is not just drawing a map. It is using location as a first-class analytical object:

- **geometry** stores where each observation is;
- **attributes** store what each observation means;
- **layers** combine multiple spatial datasets in one view;
- **filters** narrow the map to the geography relevant to the question;
- **visual inspection** turns raw coordinates into a spatial hypothesis.

That pattern will carry through the rest of the course. Coordinate reference systems keep spatial measurements honest. Interactive maps make dense geography easier to inspect. Geometric operations modify and combine spatial objects. Proximity analysis turns "near what?" into a model-ready feature or a decision rule.

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
   Filter, join, buffer, overlay, measure
              |
              v
        Layered map
   basemap + points + polygons + style
              |
              v
 Spatial pattern, service area, risk zone, or site decision
```

The key habit is to ask whether the operation depends on geometry. Filtering by `country` is ordinary tabular selection. Plotting the result on a country boundary, calculating distance, or asking which features fall within a region is geospatial analysis.

## Lesson Tracker

| # | Lesson | Status | Evidence |
|:-:|--------|:------:|----------|
| 1 | Your First Map | **Complete** | [YourFirstMapExercise.py](./YourFirstMapExercise.py) |
| 2 | Coordinate Reference Systems | **Complete** | [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py) |
| 3 | Interactive Maps | Pending | Not archived yet |
| 4 | Manipulating Geospatial Data | Pending | Not archived yet |
| 5 | Proximity Analysis | Pending | Not archived yet |

### Course trajectory

```text
Load vector data
      |
Layer points on polygons
      |
Respect coordinate reference systems
      |
Inspect geography interactively
      |
Transform and combine geometries
      |
Measure proximity for decisions
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

## Skills Practiced

From the first two solved exercises:

- Loading shapefile data with `gpd.read_file`
- Treating a `GeoDataFrame` as a DataFrame plus geometry
- Inspecting loaded spatial records with `.head()`
- Creating point geometry from longitude and latitude with `gpd.points_from_xy`
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
| Written interpretation | Converts a visualization into an analytical claim | The work stops at plotting instead of analysis |

## Geospatial Analysis Playbook

This is the workflow the course is beginning to build.

1. **Identify the spatial unit.** Know whether each row is a point, line, polygon, grid cell, address, or administrative region.
2. **Load geometry and attributes together.** Prefer spatial readers such as `gpd.read_file` when a file already encodes geometry.
3. **Inspect before plotting.** Check columns, geometry type, row count, missing values, and coordinate reference system.
4. **Choose the right map scale.** A global plot is useful for context; a regional plot is better for local patterns.
5. **Layer deliberately.** Draw context first, then observations, then highlights or annotations.
6. **Preserve CRS meaning.** Assign the source CRS, align layers before plotting, and do not measure distance or area until the CRS makes those units valid.
7. **Use spatial operations when the question is spatial.** Buffers, joins, overlays, and distances should answer geography-driven questions, not replace simple tabular filters.
8. **Interpret the map.** State the visible pattern, the uncertainty, and the decision it supports.
9. **Record assumptions.** Include projection, filters, data vintage, and any simplification or aggregation that could affect the result.

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
| Spatial filter | Selection based on location, intersection, containment, or distance |
| Spatial join | Attribute merge driven by geometry relationships instead of a shared key |
| Buffer | New geometry representing a fixed distance around existing geometry |

## Artifacts

- [YourFirstMapExercise.py](./YourFirstMapExercise.py) - loads Kiva loan shapefile data, plots loan points over a world basemap, filters loans in the Philippines, plots them over a Philippines basemap, and records a regional concentration reading.
- [CoordinateReferenceSystemsExercise.py](./CoordinateReferenceSystemsExercise.py) - creates bird-location point geometry from longitude/latitude columns, assigns EPSG:4326 CRS metadata, plots migration starts, paths, and endpoints, loads protected-area polygons, reprojects South America before area calculation, and overlays Southern Hemisphere bird observations with non-marine protected areas.

No completion certificate is present yet because the course is still in progress.

## Course Notes

- The exported `*Exercise.py` files preserve solved Kaggle notebook cells. They are reference material, not guaranteed standalone scripts, because Kaggle provides datasets, preloaded GeoDataFrames such as `world`, `PHL`, `americas`, `start_gdf`, and `path_gdf`, GeoPandas setup, plotting context, and answer-checking helpers such as `q_1.check()`.
- The CRS exercise uses the course's `{"init": "epsg:4326"}` style because that is what the notebook prompt expects. In modern GeoPandas code, `set_crs(epsg=4326)` is usually clearer when assigning a CRS to geometry that already has coordinates but lacks metadata.
- The first lesson uses vector data. The shapes are not pixels; they are geometric objects with attributes.
- The map is analytical because each plotted point is tied back to a row in `world_loans`.
- The same object can be filtered like pandas data and plotted like spatial data, which is the practical value of GeoPandas.
- The second lesson makes coordinate reference systems explicit before serious distance or area reasoning. EPSG:4326 is useful for storing and plotting latitude/longitude positions, but projected CRSs are required when the numeric units need to represent meters or square meters.
- The protected-area overlay is a visual coverage check, not a formal spatial join yet. A later lesson should replace visual proximity with explicit geometry operations.

## Next Work

- Add the interactive-map workflow once Folium maps are saved.
- Extend the playbook with spatial joins, buffers, and proximity features after those lessons are complete.
- Update the repository roadmap once Geospatial Analysis moves from "up next" to active progress.

<div align="center">

[Back to Roadmap](../README.md)

</div>
