# Smart Home Monitor (Rule-Based Simulation)

A small Python project that simulates smart home sensor readings and classifies the system status in real time using simple rule-based logic.

> **Note:** This is an early project (my first Python simulation). It uses fixed rules, not machine learning. For a machine learning project, see my [Neural Restaurant Recommender](https://github.com/aygulai-dev/neural-restaurant-recommender).

## Features

- Simulated sensors: temperature, humidity, energy consumption
- Live loop that generates a new reading every 2 seconds
- Rule-based risk score (0–3) and status classification: 🟢 Normal · 🟡 Warning · 🔴 Critical
- All readings logged to `readings.csv`
- Clean exit with `Ctrl + C`
- Unit tests for the rule logic

## Rules

One point is added for each violated rule:

| Sensor | Rule | Meaning |
|---|---|---|
| Temperature | > 30 °C | too hot |
| Energy | > 500 W | high consumption |
| Humidity | < 30 % | too dry |

| Risk score | Status |
|---|---|
| 0 | 🟢 NORMAL |
| 1 | 🟡 WARNING |
| 2–3 | 🔴 CRITICAL |

Thresholds are defined as constants at the top of `rules.py`.

## Project structure

```
.
├── data.py          # generates random sensor values
├── rules.py         # thresholds, risk score, status label
├── main.py          # live loop, console output, CSV logging
├── test_rules.py    # tests for the rule logic
└── README.md
```

## How to run

```bash
python main.py          # start the live simulation (stop with Ctrl + C)
python test_rules.py    # run the tests
```

No external libraries are required (Python standard library only).

Example console output:

```
===================================
SMART HOME MONITOR (LIVE)
===================================
Temperature: 34°C
Humidity:    52%
Energy:      541W
🔴 Status: CRITICAL
===================================
```

## Limitations

- Sensor values are randomly generated, not read from real devices.
- The rules are fixed thresholds chosen by hand; nothing is learned from data.
- Readings are independent of each other (no trends or time dependence).

## What I learned

- Structuring a Python project into separate modules
- Keeping settings (thresholds) in one place
- Writing simple tests and logging data to CSV
- How a basic decision system works, and where its limits are

## Possible improvements

- Add time-dependent sensor behaviour (e.g. temperature drifting slowly)
- Learn thresholds or detect anomalies from data instead of fixed rules
- Read data from a real sensor or an API
