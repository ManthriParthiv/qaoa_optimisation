import numpy as np
import matplotlib.pyplot as plt

def display_results(result):
    """
    Displays the optimal solution and its corresponding value.
    Also plots the solution as a bar chart.
    """
    print("Optimal solution:", result.x)
    print("Optimal value:", result.fval)
    
    # Get the results as a dictionary to handle fractional solutions if they occur
    solution_dict = result.get_counts() or {tuple(result.x.astype(int)): 1.0}
    
    # Plot the solution
    plot_solution(solution_dict)


def plot_solution(solution_dict):
    """
    Plots the solution as a bar chart.
    """
    if not solution_dict:
        print("No solution to plot.")
        return

    # Convert keys (tuples of integers) to bitstrings for plotting
    bitstrings = [''.join(map(str, x)) for x in solution_dict.keys()]
    counts = list(solution_dict.values())
    
    # Sort the results for better visualization
    sorted_results = sorted(zip(bitstrings, counts), key=lambda x: x[1], reverse=True)
    sorted_bitstrings, sorted_counts = zip(*sorted_results)

    plt.figure(figsize=(10, 6))
    plt.bar(sorted_bitstrings, sorted_counts, color='teal')
    plt.xlabel("Portfolio Selection (bitstring)", fontsize=12)
    plt.ylabel("Probability/Occurrences", fontsize=12)
    plt.title("QAOA Results for Portfolio Optimization", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()