# MSCS_532_Assignment5

# Quicksort Analysis

## Overview
This project implements and compares two versions of the Quicksort algorithm: 
1. **Deterministic Quicksort**: Uses the middle element of the array as the pivot.
2. **Randomized Quicksort**: Randomly selects a pivot from the array.

It also includes empirical analysis and visualization of the execution times for both versions on different types of input distributions (random, sorted, and reverse-sorted arrays).

---

## Features
1. **Deterministic Quicksort**:
   - Implements the Quicksort algorithm with a fixed pivot (middle element).
   - Simple and predictable, but susceptible to worst-case performance for specific input patterns.

2. **Randomized Quicksort**:
   - Implements the Quicksort algorithm with a random pivot selection.
   - Mitigates the likelihood of encountering the worst-case performance.

3. **Performance Measurement**:
   - Measures the execution time of both versions of Quicksort on different array sizes and distributions.

4. **Visualization**:
   - Generates comparative performance plots for deterministic and randomized Quicksort.

---

## Code Structure
### Functions
- **`deterministic_quicksort(arr)`**:
  - Sorts an array using the deterministic Quicksort algorithm.
  - Pivot: Middle element of the array.

- **`randomized_quicksort(arr)`**:
  - Sorts an array using the randomized Quicksort algorithm.
  - Pivot: Randomly selected element.

- **`measure_time(sort_func, arr)`**:
  - Measures the execution time of a sorting function for a given array.

- **`plot_results(results_df, cols, title)`**:
  - Plots performance results for deterministic and randomized Quicksort.

### Data
- **`sizes`**:
  - A list of input sizes for testing the performance of the sorting algorithms.
- **`results`**:
  - A list of dictionaries containing performance metrics for each input size and distribution.

---

## Usage
1. **Run the Code**:
   - Execute the script to compare deterministic and randomized Quicksort algorithms.
   - The results will be displayed as a table and visualized as performance plots.

2. **Input Distributions**:
   - Randomly generated array.
   - Pre-sorted array.
   - Reverse-sorted array.

3. **Visualization**:
   - Compare performance on different input sizes and distributions:
     - Random inputs.
     - Sorted inputs.
     - Reverse-sorted inputs.

---

## Empirical Results
The script outputs:
1. **Execution Times**:
   - Measures how deterministic and randomized Quicksort perform on various input types and sizes.
2. **Plots**:
   - Comparative plots for each input type.

---

## Requirements
- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`

Install dependencies using:
```bash
pip install numpy pandas matplotlib
