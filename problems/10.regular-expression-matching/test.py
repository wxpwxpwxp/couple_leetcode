import unittest
from siri import Solution

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertTrue(s.isMatch('aab', 'c*a*b'))
      self.assertFalse(s.isMatch('mississippi', 'mis*is*p*.'))
      self.assertTrue(s.isMatch('ahginragranoginaogi', '.*'))

if __name__ == '__main__':
    unittest.main()
