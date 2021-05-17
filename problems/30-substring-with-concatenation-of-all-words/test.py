import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.findSubstring(
            'barfoothefoobarman', ['foo', 'bar']), [0, 9])
        self.assertEqual(s.findSubstring(
            'wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']), [])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
