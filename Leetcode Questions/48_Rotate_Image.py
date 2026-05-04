#Solution 

'''
Approach

First, take the transpose of the matrix:

Swap elements across the diagonal
matrix[i][j]↔matrix[j][i]
Then, reverse each row:

Swap elements symmetrically in each row
This avoids extra space and modifies the matrix in-place.

⏱️ Complexity
Time complexity: O(n 2)
Every element is visited once.

Space complexity: O(1)
In-place transformation, no extra space used.


'''

class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        for row in matrix:
            row.reverse()