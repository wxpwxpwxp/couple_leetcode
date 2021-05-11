import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.strStr('hello', 'll'), 2)
        self.assertEqual(s.strStr('aaaaa', 'bba'), -1)
        self.assertEqual(s.strStr('', ''), 0)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
