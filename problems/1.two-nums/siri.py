from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
      temp_dict = dict()
      for i in range(len(nums)):
        if target >= nums[i]:
          temp_dict[nums[i]] = i
      for key in temp_dict:
        another_key = target - key
        if another_key in temp_dict and key != another_key:
          return [temp_dict[key], temp_dict[another_key]]
