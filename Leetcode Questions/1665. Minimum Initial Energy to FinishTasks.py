# Solution 



class Solution:
    def minimumEffort(self, a: List[List[int]]) -> int:
        return reduce(lambda q,p:max(q+p[0],p[1]),sorted(a,key=lambda p:p[1]-p[0]),0)

        