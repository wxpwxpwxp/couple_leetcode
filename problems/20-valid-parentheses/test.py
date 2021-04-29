import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertTrue(s.isValid('()'))
        self.assertTrue(s.isValid('()[]{}'))
        self.assertFalse(s.isValid('(]'))
        self.assertFalse(s.isValid('([)]'))
        self.assertTrue(s.isValid('{[]}'))

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
