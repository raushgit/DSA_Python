# Solution



class Solution:
    def minElement(self, nums: List[int]) -> int:
        res=[]
        for v in nums:
            v=list(str(v))
            v=[int(i) for i in v]
            
            res.append(sum(v))
        return min(res)
            
        