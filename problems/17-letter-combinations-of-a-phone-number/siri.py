num_letter_dict = {
  '2': ['a', 'b', 'c'],
  '3': ['d', 'e', 'f'],
  '4': ['g', 'h', 'i'],
  '5': ['j', 'k', 'l'],
  '6': ['m', 'n', 'o'],
  '7': ['p', 'q', 'r', 's'],
  '8': ['t', 'u', 'v'],
  '9': ['w', 'x', 'y', 'z'],
}
class Solution:
    def letterCombinations(self, digits: str):
      if len(digits) == 0: return []
      result = ['']
      for d in digits:
        _result = []
        for i in result:
          for dd in num_letter_dict[d]:
            _result.append(i + dd)
        result = _result
      return result
