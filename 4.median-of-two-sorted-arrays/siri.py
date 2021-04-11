from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
      toal_lenght = len(nums1) + len(nums2)
      is_odd = toal_lenght % 2 == 1
      target_index = int(toal_lenght / 2) - 1
      nums1_index = 0
      nums2_index = 0
      current = 0
      for i in range(target_index + 1):
        if not nums1_index == len(nums1) and nums1[nums1_index] < nums2[nums2_index]:
          current = nums1[nums1_index]
          nums1_index += 1
        else:
          current = nums2[nums2_index]
          nums2_index += 1

      if is_odd:
        return current
      else:
        current_next = 0
        if nums1_index == len(nums1):
          current_next = nums2[nums2_index]
        elif nums2_index == len(nums2):
          current_next = nums1[nums1_index]
        elif nums1[nums1_index] < nums2[nums2_index]:
          current_next = nums1[nums1_index]
        else:
          current_next = nums2[nums2_index]

        return (current + current_next) / 2


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3 ,4]))
