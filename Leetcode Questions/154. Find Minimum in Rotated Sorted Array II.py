#Solution 


'''

Approach:
Using the binary searchvia left and right pointers. Comparing middle with the right element. Then, moving pointers accordingly, and when duplicate occur, reduce right by one to avoid ambiguity.

Complexity

Time complexity: O(log n)
Worst case O(n) due to duplicate which can cause linear shrinkage

Space complexity: O(1)
Only Pointer variables are used in this program

Algorithm Used:
Binary Search (Modified)
Divide and Conquer


'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
        