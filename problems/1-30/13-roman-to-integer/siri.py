num_dict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

s_num_dict = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


class Solution:
    def romanToInt(self, s: str):
        s_list = list(s)
        result = 0
        skip = False
        for i in range(len(s_list) - 1):
            if skip:
                skip = False
                continue
            if s_list[i] + s_list[i + 1] in s_num_dict:
                result += s_num_dict[s_list[i] + s_list[i + 1]]
                skip = True
            else:
                result += num_dict[s_list[i]]
        if skip:
            return result
        else:
            return result + num_dict[s_list[len(s_list) - 1]]
