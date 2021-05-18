# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: List, l2: List):
        current_1 = self.generateLink(l1).next
        current_2 = self.generateLink(l2).next
        result_current = result_head = ListNode()
        while current_1 != None or current_2 != None:
            if current_1 == None:
                result_current.next = current_2
                break
            if current_2 == None:
                result_current.next = current_1
                break
            if current_1.val < current_2.val:
                result_current.next = current_1
                current_1 = current_1.next
            else:
                result_current.next = current_2
                current_2 = current_2.next
            result_current = result_current.next

        result = []
        current = result_head.next
        while current != None:
            result.append(current.val)
            current = current.next

        return result

    def generateLink(self, l: List):
        head = current = ListNode()
        for i in l:
            current.next = ListNode(i)
            current = current.next
        return head
