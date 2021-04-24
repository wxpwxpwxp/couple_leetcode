import unittest
from typing import List
from .siri import Solution
class TestStringMethods(unittest.TestCase):
    def isListEqual(self, list1: List[int], list2: List[int]):
      if len(list1) != len(list2): return False
      count_1 = 0
      count_2 = 0
      for i in list1:
        if i in list2:
          count_1 += 1
      for i in list2:
        if i in list1:
          count_2 += 1
      return count_1 == len(list1) and count_2 == len(list2)

    def isDoubleListEqual(self, list1: List[List[int]], list2: List[List[int]]):
      if len(list1) != len(list2): return False
      count_1 = 0
      count_2 = 0
      for i in list1:
        for j in list2:
          if self.isListEqual(i, j):
            count_1 += 1
      for i in list2:
        for j in list1:
          if self.isListEqual(i, j):
            count_2 += 1
      return count_1 == len(list1) and count_2 == len(list2)


    def test_siri(self):
      s = Solution()
      # self.assertEqual(s.fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
      self.assertEqual(s.fourSum([], 0), [])
      self.assertTrue(self.isDoubleListEqual(s.fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))


    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
