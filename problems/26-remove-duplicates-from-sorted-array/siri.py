from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]):
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                for j in range(i + 1, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums.pop()
                continue
            i += 1
        return len(nums)
