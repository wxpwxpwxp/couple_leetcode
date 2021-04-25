import unittest
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
