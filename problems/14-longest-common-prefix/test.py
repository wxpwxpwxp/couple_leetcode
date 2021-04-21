import unittest
from .siri import Solution
class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]), 'fl')
      self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]), '')


    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
