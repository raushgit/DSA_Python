# Solution


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)

        # Cap elements at array size since the answer cannot exceed it.
        for num in arr:
            counts[min(num, n)] += 1

        max_num = 0

        # Successively build the maximum valid element up to each index.
        for i in range(1, n + 1):
            max_num = min(max_num + counts[i], i)

        return max_num