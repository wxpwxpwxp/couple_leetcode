import unittest
from .siri import Solution
from .wxp import repeat_str


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring('abcabcbb'), 3)

    def test_wxp(self):
        self.assertEqual(repeat_str('abcabcbb'), 3)


if __name__ == '__main__':
    unittest.main()
