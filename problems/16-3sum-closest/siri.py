from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int):
        result = nums[0] + nums[1] + nums[2]
        has_find_dict = dict()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] in has_find_dict:
                    continue
                for z in range(j + 1, len(nums)):
                    if nums[z] in has_find_dict:
                        continue
                    if abs(nums[i] + nums[j] + nums[z] - target) < abs(result):
                        result = nums[i] + nums[j] + nums[z]

        has_find_dict[i] = True

        return result
