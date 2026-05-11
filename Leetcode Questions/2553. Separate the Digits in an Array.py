# Solution 




class Solution:
    def separateDigits(self, a: List[int]) -> List[int]:
        return [int(c) for v in a for c in str(v)]