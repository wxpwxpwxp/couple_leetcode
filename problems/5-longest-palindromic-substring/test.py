import unittest
from .siri import Solution
from .wxp import re_str

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.longestPalindrome('babad'), 'bab')

    def test_wxp(self):
      self.assertEqual(''.join(re_str('babad')), 'bab')

if __name__ == '__main__':
    unittest.main()
