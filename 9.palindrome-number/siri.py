class Solution:
    def isPalindrome(self, x: int):
      x_s = str(x)
      x_s_reverse = list(x_s)
      x_s_reverse.reverse()
      return x_s == ''.join(x_s_reverse)
