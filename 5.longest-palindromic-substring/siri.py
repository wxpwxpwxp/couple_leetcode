class Solution:
    def longestPalindrome(self, s: str):
      s_dict = list(s)
      reference = []
      longest = 1
      target_index = 0
      for i in range(len(s_dict)):
        if i == 0:
          longest = 1
          target_index = 0
          continue

        start_index = end_index = i
        current_lenght = 0
        start_index -= 1
        end_index += 1
        while start_index >= 0 and end_index < len(s_dict):
          if s_dict[start_index] == s_dict[end_index]:
            current_lenght = end_index - i + 1
            if current_lenght > longest:
              target_index = i
              longest = current_lenght
          else:
            break

          start_index -= 1
          end_index += 1

      result = ''
      for i in range(target_index - longest + 1, target_index + longest):
        result += s_dict[i]
      return result





s = Solution()
print(s.longestPalindrome('babad'))
