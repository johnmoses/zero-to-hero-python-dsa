""" 
Knapsack algorithm

A naive solution of the 0-1 problem

Write a basic knapsack algorithm that can be used 
to solve the 0-1 knapsack problem.

The algorithm should take in a list of items, each with a weight and a value,
as well as the maximum weight capacity of the knapsack.
The algorithm should return the maximum value that can be stored in the knapsack.

For example, given the following items:
    
    items = [
        {"weight": 2, "value": 3},
        {"weight": 3, "value": 4},
        {"weight": 4, "value": 5},
        {"weight": 5, "value": 6}

    capacity = 5
The algorithm should return 9 (max value of 3 + 4 + 5 = 12 can be stored in the knapsack with a capacity of 5).
"""

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dynamic programming table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value that can be stored in the knapsack
    return dp[n][capacity]

print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))