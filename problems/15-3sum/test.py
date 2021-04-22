import unittest
from .siri import Solution
class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2],[-1, 0, 1]])
      self.assertEqual(s.threeSum([]), [])
      self.assertEqual(s.threeSum([0]), [])

    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
