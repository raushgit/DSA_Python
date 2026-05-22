#Solution


class Solution:
    def search(self, nums: List[int], tg: int) -> int:
        imn = bisect_left(nums, True, key=lambda x: x<nums[0])
        itg = bisect_left(nums, tg, lo=(imn if tg<nums[0] else 0), hi=(None if tg<nums[0] else imn-1))
        return  itg  if tg == nums[itg%len(nums)]  else -1
        