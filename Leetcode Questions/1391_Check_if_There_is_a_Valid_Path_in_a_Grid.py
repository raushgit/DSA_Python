# Solution 

# Complexity

"""
Time complexity: (m * n)
Space complexity: (m * n)

"""

# Code

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]
        }
        m,n=len(grid),len(grid[0])
        seen=[[False]*n for _ in range(m)]
        seen[0][0]=True
        q=deque([(0,0)])
        while q:
            row,col=q.popleft()
            if((row,col)==(m-1,n-1)):
                return True
            for r,c in directions[grid[row][col]]:
                ro=row+r
                co=col+c
                if(0<=ro<m and 0<=co<n and not seen[ro][co]):
                    if((r*-1,c*-1) in directions[grid[ro][co]]):
                        q.append((ro,co))
                        seen[ro][co]=True
        return False