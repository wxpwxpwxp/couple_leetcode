from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int):
      if len(nums) < 4:
        return []
      num_3_sum = dict()
      for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
          for z in range(j + 1, len(nums)):
            key = nums[i] + nums[j] + nums[z]
            temp_dict = dict()
            temp_dict['index_list'] = [i, j , z]
            temp_dict['values'] = [nums[i], nums[j], nums[z]]
            if key in num_3_sum:
              num_3_sum[key].append(temp_dict)
            else:
              num_3_sum[key] = [temp_dict]

      for key in num_3_sum:
        remove_index = []
        for i in range(len(num_3_sum[key])):
          for j in range(i + 1, len(num_3_sum[key])):
            if j in remove_index: return
            count = 0;
            for item in num_3_sum[key][i]:
              if item in num_3_sum[key][j]:
                count += 1
            if count == 3:
              remove_index.append(j)
        temp_list = []
        ii = 0
        while ii < len(num_3_sum[key]):
          if ii not in remove_index:
            temp_list.append(num_3_sum[key][ii])
          ii += 1

        num_3_sum[key] = temp_list

      marked = dict()
      result = []
      for i in range(len(nums)):
        if nums[i] in marked: continue
        key = target - nums[i]
        if key in num_3_sum:
          for item in num_3_sum[key]:
            if i in item['index_list']: continue
            if item['values'][0] in marked or item['values'][1] in marked or item['values'][2] in marked: continue
            result.append([item['values'][0], item['values'][1], item['values'][2], nums[i]])
        marked[nums[i]] = True

      return result
