import unittest
from .siri import Solution
from .wxp import maddle_number


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_wxp(self):
        self.assertEqual(maddle_number([1, 2], [3, 4]), 2.5)


if __name__ == '__main__':
    unittest.main()
