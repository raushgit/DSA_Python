# Solution 

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        
        one = set()
        two = set()
        three = set()

        seen = set(nums)

        for i in range(len(nums)):

            for t in two:
                three.add(t ^ nums[i])

            for o in one:
                two.add(o ^ nums[i])

            one.add(nums[i])

        seen.update(three)

        return (len(seen))