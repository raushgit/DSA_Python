#Solution 

'''

Approach
'''



class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_num = sorted(nums)
        expected = list(range(1, n)) + [n - 1]
        return expected == sorted_num