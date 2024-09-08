# Hotel Rooms Problem Solver and Visualizer

This repository contains Python implementations, analysis tools, and visualization solutions for the Hotel Rooms problem, a mathematical puzzle from BMC Upper's Math Contest 1, 2024/2025. The original problem can be found in this [PDF document](https://mathcircle.berkeley.edu/sites/default/files/handouts_mc/problems/2024/mc1.pdf). Please note: The contest mentiones a castle instead of a hotel.

## Problem Description

In the Hotel Rooms problem, we have three functions that generate room numbers:

1. f(n) = n
2. g(n) = 3n + 1
3. h(n) = n + 81

For each positive integer n, we consider the set of values {f(n), g(n), h(n)}. The goal is to group these values such that any two sets with a common element are merged into a single group.

## Purpose

This project serves several purposes:
1. To calculate and analyze the group formation process for the Hotel Rooms problem.
2. To visualize the growth and development of these groups over time.
3. To provide insights into the mathematical properties of this grouping process.

## Features

### Terminal Version (`bmc_hotelrooms_terminal.py`)

- Calculation of value groups up to a user-specified maximum n.
- Multiple output options:
  - No output (for performance testing)
  - Print final groups
  - Print group sizes
  - Show step-by-step development
- Integrity checking to ensure groups remain mutually exclusive.
- Plotting of group count growth over n.
- Animated visualization of the group formation process.

### Web Application Version (`bmc_hotelrooms_webapp.py`)

- Streamlit-based web interface for easy interaction.
- Real-time calculation and display of groups.
- Interactive navigation between input, development, and diagram sections.
- Filtering options for viewing specific types of group changes (merges, folds, etc.).
- Detailed information display, including collisions of new values with existing groups.
- Visualization of group count growth over n.
- Currently missing: Animated visualization of the group formation process. That's tbd.

## Repository Contents

- `bmc_hotelrooms_terminal.py`: A comprehensive script for terminal use that combines calculation, analysis, and visualization features.
- `bmc_hotelrooms_webapp.py`: Streamlit web application for interactive problem solving and visualization.

## Requirements

- Python 3.x
- matplotlib (for terminal version)
- streamlit (for web application)

To install the required packages, run:

pip install matplotlib streamlit

## Usage

### Terminal Version

Run the script:

python bmc_hotelrooms_terminal.py

You will be prompted to:
1. Enter the maximum value for n
2. Choose an output option
3. Decide whether to plot the group count diagram
4. Choose whether to show an animation
5. If animating, specify animation speed and whether to show group members

### Web Application Version

Run the Streamlit app:

streamlit run bmc_hotelrooms_webapp.py

This will open the web application in your default browser. Use the interface to:
1. Input the maximum n value
2. Navigate between Input, Development, and Diagram sections
3. Filter the development steps to focus on specific types of changes
4. View the group count diagram

## Visualization Features

- Group count growth diagram (both versions)
- Animated bar chart representing each group's size over time (terminal version)
- Interactive step-by-step development view (web version)
- Color coding and icons in web version:
  - 🔀 for merging new values into an existing group
  - ⚠️ for folding one group into another
  - ➕ for creating a new group
- Detailed information on group changes, including members of folded groups (web version)

## Contributing

Contributions to improve the algorithm, visualization, or documentation are welcome. Please feel free to submit issues or pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).
