import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.swapPairs([1, 2, 3, 4]), [2, 1, 4, 3])
        self.assertEqual(s.swapPairs([]), [])
        self.assertEqual(s.swapPairs([1]), [1])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
