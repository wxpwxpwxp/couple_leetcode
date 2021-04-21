from typing import List

class Solution:
    def dictAdd(self, nums_dict, key):
      if key in nums_dict:
        nums_dict[key] += 1
      else:
        nums_dict[key] = 1


    def threeSum(self, nums: List[int]):
      if len(nums) < 3:
        return []
      nums_dict = dict()
      for num in nums:
        self.dictAdd(nums_dict, num)
      result = []
      mark_x_has_found = dict()
      for num in nums_dict:
        mark_z_has_found = dict()
        for num_y in nums_dict:
          if num_y in mark_z_has_found or num_y in mark_x_has_found:
            continue
          if -(num_y + num) in nums_dict and -(num_y + num) not in mark_x_has_found:
            if self.isValid(nums_dict, [num, num_y, -(num_y + num)]):
              self.dictAdd(mark_z_has_found, -(num_y + num))
              result.append([num, num_y, -(num_y + num)])

        self.dictAdd(mark_x_has_found, num)

      return result

    def isValid(self, nums_dict, nums):
      temp_dict = dict()
      for num in nums:
        self.dictAdd(temp_dict, num)
      for num in temp_dict:
        if temp_dict[num] > nums_dict[num]:
          return False
      return True
