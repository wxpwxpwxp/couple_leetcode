import unittest
from siri import Solution

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertTrue(s.isPalindrome(123454321))
      self.assertFalse(s.isPalindrome(-121))

if __name__ == '__main__':
    unittest.main()
