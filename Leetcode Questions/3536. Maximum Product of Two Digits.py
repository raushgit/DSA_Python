# Solution  One Liner


class Solution:
    def maxProduct(self, n: int) -> int:
        return max(a*b  for a,b in combinations([(n//10**p)%10 for p in range(int(log10(n))+1)] ,2))
        