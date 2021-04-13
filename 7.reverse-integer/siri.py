class Solution:
    def reverse(self, x: int):
      x_list = list(str(x))
      result = ''
      for i in range(len(x_list) - 1, 0, -1):
        result += x_list[i]

      if x_list[0] == '-':
        return int(result) * -1
      else:
        return int(result + x_list[0])

s = Solution()
print(s.reverse(-123))
print(s.reverse(-123) == -321)
