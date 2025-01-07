"""
Reverse Words
"""

s = "Let's take some contest"

def reverse_words(s):
    return " ".join(i[::-1] for i in s.split())

print(reverse_words(s))

def reverse_words_1(s):
    res = s.strip().split()
    n = len(res)
    reverse(res, 0, n - 1)
    return " ".join(res)

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

print(reverse_words_1(s))