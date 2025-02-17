"""
Pascal Triangle with Dynamic approach
"""

nun_rows = 6

from typing import List

def generate(nun_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(nun_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)

        return triangle

print(generate(nun_rows))