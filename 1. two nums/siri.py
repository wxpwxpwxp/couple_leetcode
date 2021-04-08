from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int):
      temp_dict = defaultdict(bool)
      for num in nums:
        if target >= num:
          temp_dict[num] = True
      for key in temp_dict:
        another_key = target - key
        if another_key in temp_dict and key != another_key:
          return [key, another_key]
