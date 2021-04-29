left_bound = ['{', '(', '[']
right_bound = ['}', ')', ']']


def isOk(before: str, after: str):
    if before == '{':
        if after == '}':
            return True
        return False
    elif before == '(':
        if after == ')':
            return True
        return False
    else:
        if after == ']':
            return True
        return False


class Solution:
    def isValid(self, s: str):
        str_queue = []
        for i in s:
            if i in left_bound:
                str_queue.append(i)
            if i in right_bound:
                before = str_queue.pop()
                if not isOk(before, i):
                    return False
        if len(str_queue) == 0:
            return True
        return False
