""" 
Basic math

Write a simple algorithm to find the square root of a number.
"""

def square_root(n):
    """
    Finds the square root of a given number using the Newton-Raphson method.

    Args:
        n (float): The number for which the square root needs to be calculated.

    Returns:
        float: The square root of the given number.
    """
    # Initial guess for the square root
    x = n
    # Number of iterations for the Newton-Raphson method
    y = 10

    # Newton-Raphson method to find the square root
    for i in range(y):
        # Update the guess using the Newton-Raphson formula
        x = 0.5 * (x + (n / x))

    # Return the final guess as the square root
    return x

# Example usage
print(square_root(25))
print(square_root(81))
print(square_root(100))
print(square_root(144))

"""
Output:
5.0
9.0
10.0
12.0

Explanation:
The square_root function uses the Newton-Raphson method to approximate the square root of a number.
It initializes the guess (x) with the input number (n) and then iteratively updates the guess using the formula:
x = 0.5 * (x + (n / x))
The number of iterations (y) is set to 10, which is a reasonable value for most cases.
The final guess (x) is returned as the square root of a number
"""