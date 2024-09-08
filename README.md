# Hotel Rooms Problem Solver and Visualizer

This repository contains a Python implementation, analysis, and visualization tool for the Hotel Rooms problem, a mathematical puzzle involving group formation based on specific functions.

## Problem Description

In the Hotel Rooms problem, we have three functions that generate room numbers:

1. f(n) = n
2. g(n) = 3n + 1
3. h(n) = n + 81

For each positive integer n, we consider the set of values {f(n), g(n), h(n)}. The goal is to group these values such that any two sets with a common element are merged into a single group.

## Purpose

This program serves several purposes:
1. To calculate and analyze the group formation process for the Hotel Rooms problem.
2. To visualize the growth and development of these groups over time.
3. To provide insights into the mathematical properties of this grouping process.

## Features

- Calculation of value groups up to a user-specified maximum n.
- Multiple output options:
  - No output (for performance testing)
  - Print final groups
  - Print group sizes
  - Show step-by-step development
- Integrity checking to ensure groups remain mutually exclusive.
- Plotting of group count growth over n.
- Animated visualization of the group formation process.

## Repository Contents

`hotel_rooms_combined.py`: A comprehensive script that combines calculation, analysis, and visualization features.

## Requirements

- Python 3.x
- matplotlib

To install the required package, run:

pip install matplotlib

## Usage

Run the script:

python hotel_rooms_combined.py

You will be prompted to:
1. Enter the maximum value for n
2. Choose an output option
3. Decide whether to plot the group count diagram
4. Choose whether to show an animation
5. If animating, specify animation speed and whether to show group members

The script will then execute based on your choices, providing the requested outputs and visualizations.

## Visualization Features

- Group count growth diagram
- Animated bar chart representing each group's size over time
- Color coding in animation: 
  - Blue: Unchanged groups
  - Yellow: Merged groups
  - Red: Folded groups
  - Green: Newly created groups
- Text annotations showing either group size or group members
- Text box displaying new values at each step

## Contributing

Contributions to improve the algorithm, visualization, or documentation are welcome. Please feel free to submit issues or pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
