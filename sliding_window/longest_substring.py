""" 
Find Length of the Longest Substring That Doesn’t Contain Any Vowels

Input: s = "codeforintelligents"
Output: 3
Explanation: 'nts' is the longest substring that doesn't contain any vowels.
"""

s = "codeforintelligents"

def findLongestSubstring(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    maxResult = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
            print(result)
            if len(result) > len(maxResult):
                maxResult = result
        else:
            result = ""
    
    return len(maxResult)

print(findLongestSubstring(s))