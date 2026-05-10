#Solution 



class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i] = max jumps to reach i; -1 = unreachable
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            # skip unreachable index
            if dp[i] == -1:
                continue

            for j in range(i + 1, n):
                # valid jump condition
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1]