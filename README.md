<div align="center">

# Kaggle Learn - AI Track

Course-by-course notes, exported exercise solutions, and completion artifacts from the Kaggle Learn AI track.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Kaggle%20Learn-20BEFF.svg)](https://www.kaggle.com/learn)
[![Python](https://img.shields.io/badge/Python-3-3776AB.svg)](https://www.python.org/)

`[###..............] 1 in progress · 2 / 17 complete`

</div>

## Overview

This repository tracks progress through Kaggle Learn's AI and data science curriculum. Each course directory includes a course README, exported exercise solutions saved as Python files when available, and a certificate image once the course is finished.

## Roadmap

| # | Course | Hours | Status | Evidence |
|:-:|--------|:-----:|--------|----------|
| 1 | [Intro to Programming](./IntroToProgramming/) | 5h | Complete | [Certificate](./IntroToProgramming/Cux%20Prada%20-%20Intro%20to%20Programming.png) |
| 2 | [Python](./Python/) | 5h | Complete | [Certificate](./Python/Cux%20Prada%20-%20Python.png) |
| 3 | [Pandas](./Pandas/) | 4h | In Progress | [README](./Pandas/README.md) |
| 4 | Data Visualization | 4h | Next | - |
| 5 | Data Cleaning | 4h | Pending | - |
| 6 | Intro to SQL | 3h | Pending | - |
| 7 | Advanced SQL | 4h | Pending | - |
| 8 | Intro to Machine Learning | 3h | Pending | - |
| 9 | Intermediate Machine Learning | 4h | Pending | - |
| 10 | Machine Learning Explainability | 4h | Pending | - |
| 11 | Feature Engineering | 5h | Pending | - |
| 12 | Time Series | 5h | Pending | - |
| 13 | Intro to Deep Learning | 4h | Pending | - |
| 14 | Computer Vision | 4h | Pending | - |
| 15 | Geospatial Analysis | 4h | Pending | - |
| 16 | Intro to Game AI and Reinforcement Learning | 4h | Pending | - |
| 17 | Intro to AI Ethics | 4h | Pending | - |

Planned follow-up after Kaggle Learn: [Practical Deep Learning for Coders](https://course.fast.ai).

## Running the Exercises

These `*Exercise.py` files are exports of Kaggle notebook solutions rather than standalone packages.

- Many files depend on Kaggle's `learntools` checks such as `q1.check()`.
- Some exercises expect notebook-provided objects like `jimmy_slots`, `play_slot_machine`, or datasets mounted under `../input/`.
- A course folder may exist before any exercise exports are added, so early in-progress courses can contain only a `README.md`.
- For reproducible execution, run the code inside the corresponding Kaggle Learn notebook or in a local environment that mirrors Kaggle's runtime.

## Repository Structure

```text
kaggle/
├── README.md
├── LICENSE
├── IntroToProgramming/
│   ├── README.md
│   ├── *Exercise.py
│   └── Cux Prada - Intro to Programming.png
├── Pandas/
│   └── README.md
└── Python/
    ├── README.md
    ├── *Exercise.py
    └── Cux Prada - Python.png
```

Additional course folders will be added here as progress continues through the track.

## License

Released under the [MIT License](./LICENSE).
