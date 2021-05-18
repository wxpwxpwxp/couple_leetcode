import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.reverseKGroup([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5])
        self.assertEqual(s.reverseKGroup([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
        self.assertEqual(s.reverseKGroup([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(s.reverseKGroup([1], 1), [1])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
