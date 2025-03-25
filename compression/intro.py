""" 
Data compression

Write a basic data compression algorithm that takes a string and compresses it using the following rules:
Consecutive duplicate characters are replaced with a single instance of the character followed by the number of times it appears in the string.
For example, the string "aaaabbccccc" would be compressed to "a4b2c5".

The function should take a string as input and return the compressed version of the string.

Note: You can assume that the input string will only contain lowercase alphabets.
Examples:
    Input: "aaaabbccccc"
    Output: 'a4b2c5'
    Input: "abc"
    Output: 'a1b1c1'
"""

def compress(string):
    """
    Compresses a string by replacing consecutive duplicate characters with a single instance of the character followed by the number of times it appears in the string.

    Args:
        string (str): The input string to be compressed.

    Returns:
        str: The compressed string.
    """
    compressed = ""  # Initialize an empty string to store the compressed version
    count = 1  # Initialize the count of consecutive characters to 1

    # Iterate over the characters in the string, starting from the second character
    for i in range(len(string)-1):
        # If the current character is the same as the next character
        if string[i] == string[i+1]:
            count += 1  # Increment the count of consecutive characters
        else:
            # If the current character is different from the next character
            compressed = compressed + string[i] + str(count)  # Append the current character and its count to the compressed string
            count = 1  # Reset the count of consecutive characters to 1

    # Append the last character and its count to the compressed string
    compressed = compressed + string[i+1] + str(count)

    return compressed  # Return the compressed string

print(compress("aaaabbccccc"))
print(compress("abc"))