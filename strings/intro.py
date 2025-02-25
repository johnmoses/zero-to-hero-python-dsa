"""
String methods
"""

txt = "hello, and welcome to my world."

# Make the first letter upper case
x = txt.capitalize()
print('Sentence case: ', x)

# Convert to lower case
x = txt.casefold()
print('Lower: ', x)

# Find text
x = txt.find("welcome")
print('Found word at index: ', x)