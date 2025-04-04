""" 
Write code to check if string is palindrome.

A string is palindrome if it reads the same forward and backward. 
In other words, it is a palindrome if it is equal to its reverse.
"""

def is_palindrome(string):
    """
    Checks if the given string is a palindrome.

    Args:
        string (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False

print(is_palindrome("racecar"))