from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                for j in range(i + 1, len(nums)):
                    nums[j - 1] = nums[j]
                nums.pop()
                continue
            i += 1
        return len(nums)
