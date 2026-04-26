# Solution 
"""
Intuition :
The problem asks to detect a cycle in a grid where movement is allowed in 4 directions and only cells with the same character are connected. My first thought is to treat the grid as an undirected graph and use DFS to detect cycles while carefully avoiding revisiting the immediate parent cell.
"""
#### Approach :
"""
We run DFS from every unvisited cell in the grid.

During DFS:
Mark the current cell as visited.
Explore all 4 directions.
Move to a neighbor only if:
It is within grid bounds
It has the same character as the current cell
It is not the direct parent cell (to avoid trivial backtracking)

If we reach a cell that is already visited and it is not the parent, then a cycle exists.

We repeat this for all components since the grid may be disconnected.

Complexity
Time complexity: O(m×n)
Note: Each cell is visited once, and each cell checks at most 4 neighbors.

Space complexity: O(m×n)
Note: For the visited matrix and recursion stack in worst case.


"""

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visit = [False] * (m * n)
        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

        def dfs(r, c, pr, pc):
            visit[r * n + c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (nr, nc) != (pr, pc):
                    if 0 <= nr < m:
                        if 0 <= nc < n:
                            if grid[nr][nc] == grid[r][c]:
                                if visit[nr * n + nc]:
                                    return True
                                if dfs(nr, nc, r, c):
                                    return True
            return False

        for i in range(m):
            for j in range(n):
                if not visit[i * n + j]:
                    if dfs(i, j, -1, -1):
                        return True

        return False