# 此方法时间复杂度高，但是空间复杂度低
# 后续可以设计一种时间复杂度低，但是空间复杂度高的方法
class Solution:
    def lengthOfLongestSubstring(self, s: str):
      s_dict = list(s)
      s_dict_length = len(s_dict)
      if s_dict_length == 0 or s_dict_length == 1:
        return s_dict_length
      start = 0
      longest = 1
      now_long = 1
      for i in range(1, s_dict_length):
        current = s_dict[i]
        repeat = False

        for j in range(start, i):
          if(current == s_dict[j]):
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


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
