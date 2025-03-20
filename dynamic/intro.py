"""
Dynamic programming

Write a dynamic programming algorithm to find the minimum number of coins needed to make up a given amount.
The coins available are 1, 5, 10, and 25 cents.

Example usage:
    print(min_coins(11))  # Output: 3 (minimum coins: 1, 5, 6)
"""

def min_coins(amount):
    """
    Calculates the minimum number of coins needed to make up a given amount.

    Args:
        amount (int): The amount in cents for which the minimum number of coins needs to be calculated.

    Returns:
        int: The minimum number of coins needed to make up the given amount.
    """
    # Initialize a list to store the minimum number of coins needed for each amount up to the given amount
    min_coins_list = [0] * (amount + 1)

    # Iterate over each amount from 1 to the given amount
    for cents in range(1, amount + 1):
        # Initialize the minimum number of coins needed for the current amount to a large value
        coins_count = 1000000

        # Try all possible coin denominations (1, 5, 10, 25 cents)
        for j in [1, 5, 10, 25]:
            # If the current coin denomination is less than or equal to the current amount
            if cents >= j:
                # Calculate the minimum number of coins needed for the remaining amount
                # by adding 1 to the minimum number of coins needed for the remaining amount
                # after subtracting the current coin denomination
                coins_count = min(coins_count, 1 + min_coins_list[cents - j])

        # Store the minimum number of coins needed for the current amount
        min_coins_list[cents] = coins_count

    # Return the minimum number of coins needed for the given amount
    return min_coins_list[amount]
    
print(min_coins(11))  # Output: 3 (minimum coins: 1, 5, 6)