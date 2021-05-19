from typing import List


class Solution:
    result = []

    def generateParenthesis(self, n: int):
        self.result = []
        self.generate(n, n, 2 * n, '')
        result_dict = dict()
        for i in self.result:
            result_dict[i] = True
        result = []
        for i in result_dict:
            result.append(i)
        return result

    def generate(self, left: int, right: int, count: int, current: str):
        if left < 0 or right < 0 or count < 0:
            return
        if left == 0 and right == 0 and left + right == count:
            self.result.append(current)
            return
        if left != 0:
            padding_left = current
            for i in range(1, left + 1):
                padding_left += '('
                self.generate(left - i, right, count - i, padding_left)
        if left < right:
            padding_right = current
            for i in range(1, right - left + 1):
                padding_right += ')'
                self.generate(left, right - i, count - i, padding_right)
