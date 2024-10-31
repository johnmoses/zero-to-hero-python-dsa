""" 
Knapsack problem
"""

def knapsack(capacity: int, weights: list[int], values: list[int], counter: int) -> int:
    """
    Returns the maximum value that can be put in knalsack of a capacity cap,
    whereby each weight w has a specific value val.
    """
    # Define base case 
    if counter == 0 or capacity == 0:
        return 0
    # Check weights
    if weights[counter - 1] > capacity:
        return knapsack(capacity, weights, values, counter - 1)

    else:
        left_capacity = capacity - weights[counter - 1]
        new_value_included = values[counter - 1] + knapsack(
            left_capacity, weights, values, counter - 1
        )
        without_new_value = knapsack(capacity, weights, values, counter - 1)
        return max(new_value_included, without_new_value)

if __name__ == "__main__":
    import doctest

    doctest.testmod()