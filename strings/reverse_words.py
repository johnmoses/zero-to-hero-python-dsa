"""
Reverse Words
"""

def reverse_words(s: str) -> str:
    return " ".join(i[::-1] for i in s.split())

s = "Let's take some contest"
print(reverse_words(s))