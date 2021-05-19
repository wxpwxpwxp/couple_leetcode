import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.mergeTwoLists(
            [1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])
        self.assertEqual(s.mergeTwoLists([], []), [])
        self.assertEqual(s.mergeTwoLists([], [0]), [0])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
