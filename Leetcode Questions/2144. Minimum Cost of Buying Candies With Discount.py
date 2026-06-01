# Solution 


class Solution:
    def minimumCost(self, cst: List[int]) -> int:
        cst.sort(reverse=True)

        ans = 0

        for i, val in enumerate(cst):
            if i % 3 != 2:
                ans += val

        return ans