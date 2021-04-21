import unittest
from .siri import Solution

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.intToRoman(1994), 'MCMXCIV')
      self.assertEqual(s.intToRoman(58), 'LVIII')

    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
