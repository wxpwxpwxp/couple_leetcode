import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.mergeKLists(
            [[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertEqual(s.mergeKLists([]), [])
        self.assertEqual(s.mergeKLists([[]]), [])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
