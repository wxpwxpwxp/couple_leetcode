import unittest
from .siri import Solution
class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
