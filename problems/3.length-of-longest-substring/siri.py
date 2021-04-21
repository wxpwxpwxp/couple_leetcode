# 此方法时间复杂度高，但是空间复杂度低
# 后续可以设计一种时间复杂度低，但是空间复杂度高的方法
class Solution:
    def lengthOfLongestSubstring(self, s: str):
      s_list = list(s)
      s_list_length = len(s_list)
      if s_list_length == 0 or s_list_length == 1:
        return s_list_length
      start = 0
      longest = 1
      now_long = 1
      for i in range(1, s_list_length):
        current = s_list[i]
        repeat = False

        for j in range(start, i):
          if(current == s_list[j]):
            start = j + 1
            repeat = True
            break

        if repeat:
          now_long = i - start + 1
        else:
          now_long += 1
          if now_long > longest:
            longest = now_long

      return longest
