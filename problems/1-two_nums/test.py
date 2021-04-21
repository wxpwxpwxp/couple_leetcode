import unittest
from .siri import Solution
from .wxp import sum_list

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.twoSum([1, 2, 3, 4], 4), [0, 2])

    def test_wxp(self):
      self.assertEqual(sum_list([1, 2, 3, 4], 4), [0, 2])

if __name__ == '__main__':
    unittest.main()
