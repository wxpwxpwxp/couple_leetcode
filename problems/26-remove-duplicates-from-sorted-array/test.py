import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
