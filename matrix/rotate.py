"""
Rotate a matrix

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-j-1]
            matrix[n-1-i][n-j-1] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]
            matrix[i][j] = tmp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))