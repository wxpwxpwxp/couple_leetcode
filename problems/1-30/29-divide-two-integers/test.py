import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.divide(10, 3), 3)
        self.assertEqual(s.divide(7, -3), -2)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
