import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.removeElement([3, 2, 2, 3], 3), 2)
        self.assertEqual(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
