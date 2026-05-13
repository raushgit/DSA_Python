# Solution 



# Approach 

'''
Approach
For each pair (a, b):

Initially assume every target sum requires 2 moves.
Determine the range of sums that can be achieved with:
1 move
0 moves

For a pair:

Minimum possible sum with one move:

min(a, b) + 1

Maximum possible sum with one move:

max(a, b) + limit

Exact sum needing 0 moves:

a + b

We use a difference array (delta) to mark how the move count changes over ranges:

Add +2 for all sums initially.
Reduce by 1 for the range achievable in one move.
Reduce another 1 at a + b because that sum needs zero moves.
Restore values after the valid ranges end.

Finally, we compute prefix sums over all target sums to get the minimum total moves.

Complexity
Time complexity:
O(n + limit)
Space complexity:
O(limit)


'''

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = collections.Counter()
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1  #please upvote #
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
            
        curr = 0            
        res = math.inf
        for i in range(2, 2 * limit + 1):
            curr += delta[i]
            res = min(res, curr)
        return res   #please upvote #