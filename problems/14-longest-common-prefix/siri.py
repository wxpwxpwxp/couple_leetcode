from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        shortest_lenght = len(strs[0])
        for _str in strs:
            if(len(_str) < shortest_lenght):
                shortest_lenght = len(_str)
        result = ''
        for i in range(shortest_lenght):
            ref = strs[0][i]
            for j in range(1, len(strs)):
                if ref != strs[j][i]:
                    return result
            result += ref
        return result
