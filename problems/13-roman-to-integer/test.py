import unittest
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.romanToInt('MCMXCIV'), 1994)
        self.assertEqual(s.romanToInt('LVIII'), 58)

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
