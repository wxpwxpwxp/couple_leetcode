from typing import List
from copy import deepcopy


def genNext(words: List[str], value: str, result: List[str]):
    if len(words) == 0:
        result.append(value)

    for i in range(len(words)):
        _words = deepcopy(words)
        _word = _words.pop(i)
        genNext(_words, value + _word, result)


class Solution:
    def findSubstring(self, s: str, words: List[str]):
        words_length = 0
        for word in words:
            words_length += len(word)
        words = self.genAllSubstring(words)
        result = []
        for i in range(len(s) - words_length):
            if s[i:i + words_length] in words:
                result.append(i)
        return result

    def genAllSubstring(self, words: List[str]):
        result = []
        genNext(words, '', result)
        return result
