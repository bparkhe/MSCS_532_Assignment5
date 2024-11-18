import random
import time
import numpy as np

def deterministic_quicksort(arr):
    """
    Deterministic Quicksort where pivot is the middle element.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

def randomized_quicksort(arr):
    """
    Randomized Quicksort where pivot is chosen randomly.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Empirical analysis
def measure_time(sort_func, arr):
    """
    Measures the execution time of a sorting function.
    """
    start = time.time()
    sort_func(arr)
    return time.time() - start

# Generate test cases
sizes = [100, 500, 1000, 5000, 10000]
results = []

for size in sizes:
    random_array = np.random.randint(0, 100000, size).tolist()
    sorted_array = sorted(random_array)
    reverse_sorted_array = sorted_array[::-1]

    results.append({
        "size": size,
        "deterministic_random": measure_time(deterministic_quicksort, random_array),
        "deterministic_sorted": measure_time(deterministic_quicksort, sorted_array),
        "deterministic_reverse": measure_time(deterministic_quicksort, reverse_sorted_array),
        "randomized_random": measure_time(randomized_quicksort, random_array),
        "randomized_sorted": measure_time(randomized_quicksort, sorted_array),
        "randomized_reverse": measure_time(randomized_quicksort, reverse_sorted_array),
    })

import pandas as pd

# Convert results to DataFrame for visualization
results_df = pd.DataFrame(results)
import ace_tools as tools; tools.display_dataframe_to_user(name="Quicksort Performance Analysis", dataframe=results_df)
# Visualization for deterministic vs randomized Quicksort on various input distributions
def plot_results(results_df, cols, title):
    plt.figure(figsize=(10, 6))

    for col in cols:
        plt.plot(results_df["size"], results_df[col], label=col.replace("_", " ").title())

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Plot for random inputs
plot_results(
    results_df,
    ["deterministic_random", "randomized_random"],
    "Deterministic vs Randomized Quicksort on Random Inputs"
)

# Plot for sorted inputs
plot_results(
    results_df,
    ["deterministic_sorted", "randomized_sorted"],
    "Deterministic vs Randomized Quicksort on Sorted Inputs"
)

# Plot for reverse-sorted inputs
plot_results(
    results_df,
    ["deterministic_reverse", "randomized_reverse"],
    "Deterministic vs Randomized Quicksort on Reverse-Sorted Inputs"
)
