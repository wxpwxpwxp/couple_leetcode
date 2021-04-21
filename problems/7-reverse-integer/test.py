import unittest
from .siri import Solution
from .wxp import reverse

class TestStringMethods(unittest.TestCase):

    def test_siri(self):
      s = Solution()
      self.assertEqual(s.reverse(-123), -321)

    @unittest.skip('this method can\'t excute')
    def test_wxp(self):
      self.assertEqual(reverse(123), 321)

if __name__ == '__main__':
    unittest.main()
