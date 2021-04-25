class Solution:
    def convert(self, s: str, numRows: int):
        s_list = list(s)
        s_length = len(s_list)
        result = ''
        num_rows_add = (numRows - 1) * 2
        for i in range(numRows):
            start = i
            result += s_list[start]
            step_length = [num_rows_add - 2 * i, 2 * i]
            now_index = 0
            while start < s_length:
                if step_length[now_index] == 0:
                    now_index = 1 - now_index
                    continue
                elif start + step_length[now_index] < s_length:
                    start += step_length[now_index]
                    result += s_list[start]
                    now_index = 1 - now_index
                else:
                    break
        return result
