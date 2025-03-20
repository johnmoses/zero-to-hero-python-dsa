"""
Count the number of characters in a string

Write a simple string algorithm

The algorithm should take a string as input and return the number of characters in the string.
"""

def countCharacters(string):
    """
    Counts the number of characters in a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The number of characters in the string.
    """
    # Initialize a counter variable to keep track of the number of characters
    counter = 0
    
    # Iterate over each character in the string
    for char in string:
        # Increment the counter for each character
        counter += 1
    
    # Return the final count of characters
    return counter

print(countCharacters("Hello"))

