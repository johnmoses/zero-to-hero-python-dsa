"""
Maximum Distance
"""

from typing import List

def max_distance(colors: List[int]) -> int:
    mp = {}
    maxDict = 0
    n = 7
    for i in range(n):
        if colors[i] not in mp.keys():
            mp[colors[i]] = i
        else:
            maxDict = max(maxDict, i-mp[colors[i]])
    return maxDict

colors = [1,1,1,6,1,1,1]
print(max_distance(colors))