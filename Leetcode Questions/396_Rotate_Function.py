#Solution 

#Approach 



#Code 

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        prev = 0 
        for i in range (n):
            prev += nums[i]*i
        res = prev 
        for i in range(n-1,-1,-1):
            prev= prev +(total-nums[i])-(n-1)*nums[i]
            res = max(res ,prev)
        return res
        