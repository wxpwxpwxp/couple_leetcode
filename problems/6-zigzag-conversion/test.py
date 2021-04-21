import unittest
from .siri import Solution

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

    def test_wxp(self):
      return

if __name__ == '__main__':
    unittest.main()
