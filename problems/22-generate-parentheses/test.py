import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(
            3), ['((()))', '(()())', '(())()', '()(())', '()()()'])
        self.assertEqual(s.generateParenthesis(
            1), ['()'])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
