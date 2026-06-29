<div align="center">

# Geospatial Analysis

**Course 15 of 17 - mapping data, preserving location meaning, and turning geometry into analytical evidence.**

[![Kaggle](https://img.shields.io/badge/Kaggle-Geospatial%20Analysis-20BEFF.svg)](https://www.kaggle.com/learn/geospatial-analysis)
![Status](https://img.shields.io/badge/Status-In%20Progress-f5b642.svg)
![Lessons](https://img.shields.io/badge/Lessons-1%20of%205-f5b642.svg)
[![GeoPandas](https://img.shields.io/badge/GeoPandas-ready-139C5A.svg)](https://geopandas.org/)

`PLACE -> GEOMETRY -> LAYER -> PATTERN -> DECISION`

[Course Snapshot](#course-snapshot) . [Mental Model](#the-core-mental-model) . [Lessons](#lesson-tracker) . [First Map](#implemented-first-map) . [Skills](#skills-practiced) . [Playbook](#geospatial-analysis-playbook) . [Artifacts](#artifacts)

</div>

---

## Course Snapshot

| Field | Detail |
|-------|--------|
| Position | Course 15 of 17 |
| Estimated time | 4 hours |
| Status | **In progress - 1 of 5 lessons archived** |
| Started | June 29, 2026 |
| Current lesson | Your First Map |
| Core library | GeoPandas |
| Task introduced | Loading vector geospatial data, plotting layered maps, filtering locations, and reading spatial concentration |
| Running dataset | Kiva loan locations from shapefiles, paired with world and Philippines basemap geometry |
| Repository artifacts | 1 lesson export |
| Course page | [Kaggle Learn: Geospatial Analysis](https://www.kaggle.com/learn/geospatial-analysis) |
| Prerequisite context | [Data Visualization](../4_DataVisualization/), [Pandas](../3_Pandas/), and general feature-engineering discipline |

> **Repository truth:** this directory currently contains the first official lesson export only. The README tracks the full course path, but only [YourFirstMapExercise.py](./YourFirstMapExercise.py) is backed by saved local work so far.

## What This Course Adds

Earlier courses treat most rows as independent observations with ordinary scalar features. Geospatial Analysis adds a new type of feature: **place**. A row can now carry geometry - a point, line, or polygon - and that geometry changes what questions are possible.

The first exercise makes the shift concrete. A shapefile is loaded into a `GeoDataFrame`, the geometry column is plotted as point data, and those points are layered over boundary polygons to make the pattern readable. The important move is not just drawing a map. It is using location as a first-class analytical object:

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
| 2 | Coordinate Reference Systems | Pending | Not archived yet |
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

## Skills Practiced

From the first solved exercise:

- Loading shapefile data with `gpd.read_file`
- Treating a `GeoDataFrame` as a DataFrame plus geometry
- Inspecting loaded spatial records with `.head()`
- Plotting country boundary polygons with GeoPandas
- Plotting point geometries on top of an existing matplotlib axis
- Controlling map context with `figsize`, `color`, `linestyle`, and `edgecolor`
- Keeping layer order deliberate so basemap polygons do not hide point data
- Filtering geospatial records with `.loc`
- Selecting country-specific rows with `.isin(["Philippines"])`
- Reusing the same plotting pattern at global and national scales
- Separating data loading, filtering, visualization, and interpretation into distinct steps
- Reading spatial concentration as evidence rather than treating the map as decoration
- Preserving Kaggle answer checks alongside solved notebook cells

## Why Each Choice Matters

| Choice | Role | If it is wrong |
|--------|------|----------------|
| `gpd.read_file` | Loads vector geometry and attributes together | Location columns may be lost or treated as plain text |
| Shapefile input | Provides points, metadata, and spatial reference as a dataset bundle | Missing companion files can make the read fail or strip spatial meaning |
| Polygon basemap | Gives the point layer geographic context | Points appear as an unanchored cloud |
| Shared matplotlib axis | Places multiple GeoDataFrames in one map | Each layer appears in a separate figure instead of one composition |
| Basemap first, points second | Keeps observations visible above the background | Polygons can cover the data being analyzed |
| Small point marker size | Makes dense global data readable | Large markers can hide clustering and overlap |
| Country filter | Narrows the analysis to the question's geography | Global scale can hide the local pattern |
| Country-specific basemap | Gives the filtered points useful local context | The viewer must infer boundaries and regions mentally |
| Written interpretation | Converts a visualization into an analytical claim | The work stops at plotting instead of analysis |

## Geospatial Analysis Playbook

This is the workflow the course is beginning to build.

1. **Identify the spatial unit.** Know whether each row is a point, line, polygon, grid cell, address, or administrative region.
2. **Load geometry and attributes together.** Prefer spatial readers such as `gpd.read_file` when a file already encodes geometry.
3. **Inspect before plotting.** Check columns, geometry type, row count, missing values, and coordinate reference system.
4. **Choose the right map scale.** A global plot is useful for context; a regional plot is better for local patterns.
5. **Layer deliberately.** Draw context first, then observations, then highlights or annotations.
6. **Preserve CRS meaning.** Do not measure distance or area until the coordinate reference system makes those units valid.
7. **Use spatial operations when the question is spatial.** Buffers, joins, overlays, and distances should answer geography-driven questions, not replace simple tabular filters.
8. **Interpret the map.** State the visible pattern, the uncertainty, and the decision it supports.
9. **Record assumptions.** Include projection, filters, data vintage, and any simplification or aggregation that could affect the result.

## GeoDataFrame Reference

| Concept | Meaning |
|---------|---------|
| Attribute columns | Ordinary tabular fields such as country, amount, category, or date |
| Geometry column | Spatial object attached to each row, usually points, lines, or polygons |
| CRS | Coordinate reference system that defines what coordinate values mean |
| Layer | One plotted spatial dataset in a map composition |
| Basemap | Context layer used to orient the main analytical layer |
| Spatial filter | Selection based on location, intersection, containment, or distance |
| Spatial join | Attribute merge driven by geometry relationships instead of a shared key |
| Buffer | New geometry representing a fixed distance around existing geometry |

## Artifacts

- [YourFirstMapExercise.py](./YourFirstMapExercise.py) - loads Kiva loan shapefile data, plots loan points over a world basemap, filters loans in the Philippines, plots them over a Philippines basemap, and records a regional concentration reading.

No completion certificate is present yet because the course is still in progress.

## Course Notes

- The exported `*Exercise.py` file preserves solved Kaggle notebook cells. It is reference material, not a guaranteed standalone script, because Kaggle provides datasets, preloaded basemap GeoDataFrames such as `world` and `PHL`, GeoPandas setup, plotting context, and answer-checking helpers such as `q_1.check()`.
- The first lesson uses vector data. The shapes are not pixels; they are geometric objects with attributes.
- The map is analytical because each plotted point is tied back to a row in `world_loans`.
- The same object can be filtered like pandas data and plotted like spatial data, which is the practical value of GeoPandas.
- The next lesson should make coordinate reference systems explicit before any serious distance or area reasoning is attempted.

## Next Work

- Archive the Coordinate Reference Systems exercise.
- Record CRS transformations and the difference between plotting coordinates and measurement coordinates.
- Add the interactive-map workflow once Folium maps are saved.
- Extend the playbook with spatial joins, buffers, and proximity features after those lessons are complete.

<div align="center">

[Back to Roadmap](../README.md)

</div>
