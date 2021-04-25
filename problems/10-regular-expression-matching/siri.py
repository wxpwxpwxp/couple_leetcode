class MatchNode:
    def __init__(self, val=0, modify='', next=None):
        self.val = val
        self.modify = modify
        self.next = next

    def printNode(self):
        print(self.val, self.modify)
        if self.next is not None:
            self.next.printNode()


def isEqual(a, reg):
    if reg == '.':
        return True
    else:
        return a == reg


class Solution:
    def isMatch(self, s: str, p: str):
        p_list = list(p)
        head = MatchNode(p_list[0])
        current = head
        for i in range(1, len(p_list)):
            if p_list[i] == '*':
                current.modify = '*'
            else:
                current.next = MatchNode(p_list[i])
                current = current.next

        current = head
        s_index = 0
        while(current is not None and s_index < len(s)):
            if current.modify == '':
                if not isEqual(s[s_index], current.val):
                    return False
                s_index += 1
            else:
                while(s_index < len(s) and isEqual(s[s_index], current.val)):
                    s_index += 1
            current = current.next

        if current is None and s_index == len(s):
            return True
        else:
            return False
