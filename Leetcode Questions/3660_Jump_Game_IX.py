#Solution 



class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pref = list(accumulate(nums, max))
        nums.reverse()
        suff = list(accumulate(nums, min))
        suff.reverse()
        ans = pref
        
        for i in range(n - 2, -1, -1):
            if pref[i] > suff[i + 1]:
                ans[i] = ans[i + 1]

        return ans