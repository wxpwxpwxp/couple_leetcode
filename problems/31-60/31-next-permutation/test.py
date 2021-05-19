import unittest
from typing import List
from .siri import Solution


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        test_examples = [
            {'value': [1, 3, 2], 'res': [2, 1, 3]},
            {'value': [1, 2, 3], 'res': [1, 3, 2]},
            {'value': [1, 1, 5], 'res': [1, 5, 1]},
            {'value': [3, 2, 1], 'res': [1, 2, 3]},
            {'value': [1], 'res': [1]},
            {'value': [5, 1, 3, 4, 2], 'res': [5, 1, 4, 2, 3]}
        ]
        for example in test_examples:
            s.nextPermutation(example['value'])
            self.assertEqual(example['value'], example['res'])

    def test_wxp(self):
        return


if __name__ == '__main__':
    unittest.main()
