from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]):
        stop = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                stop = i - 1
                break
        if stop == None:
            nums.reverse()
            return

        target = stop + 1
        for i in range(stop + 1, len(nums)):
            if nums[i] > nums[stop] and nums[target] > nums[i]:
                target = i

        temp = nums[stop]
        nums[stop] = nums[target]
        nums[target] = temp

        for i in range(0, len(nums) - stop - 1):
            for j in range(stop + 1, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
