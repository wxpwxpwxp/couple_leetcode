import unittest
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(
            s.letterCombinations('23'), [
                'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
        self.assertEqual(s.letterCombinations(''), [])
        self.assertEqual(s.letterCombinations(['2']), ['a', 'b', 'c'])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
