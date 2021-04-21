num_dict = {
  1000: 'M',
  500: 'D',
  100: 'C',
  50: 'L',
  10: 'X',
  5: 'V',
  1: 'I',
}

s_num_dict = {
  4: 'IV',
  9: 'IX',
  40: 'XL',
  90: 'XC',
  400: 'CD',
  900: 'CM'
}

def getNormalRoman(num):
  result = ''
  has_find = False
  for i in num_dict:
    if i <= num and not has_find:
      result += num_dict[i]
      num = num % i
      has_find = True
      continue
    if has_find:
      for j in range(int(num / i)):
        result += num_dict[i]
      break
  return result



class Solution:
    def intToRoman(self, num: int):
      for i in [1000, 100 , 10 , 1]:
        if num >= i:
          current = int(num / i) * i
          current_roman = ''
          if current in s_num_dict:
            current_roman = s_num_dict[current]
          else:
            current_roman = getNormalRoman(current)

          if i == 1:
            return current_roman
          else:
            return current_roman + self.intToRoman(num % i)
