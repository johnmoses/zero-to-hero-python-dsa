"""
Combination with Backtracking
"""

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(first = 1, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
        for i in range(first, n + 1):
            # add i into the current combination
            curr.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    output = []
    backtrack()
    return output

n = 4
k = 2
print(combine(n, k))