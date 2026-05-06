#Solution 

class Solution:
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: simulate gravity for each row
        for i in range(m):
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][empty] = '#'
                    empty -= 1
        
        # Step 2: rotate 90° clockwise
        res = [[None] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]
        
        return res