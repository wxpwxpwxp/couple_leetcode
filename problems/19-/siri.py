from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, link_list: List, n: int):
        self.generateLink(link_list)
        ref_list = []
        current = self.head
        while current != None:
            ref_list.append(current)
            current = current.next
        ref_list[len(ref_list) - n - 1].next = ref_list[len(ref_list) - n].next
        result_list = []
        current = self.head.next
        while current != None:
            result_list.append(current.val)
            current = current.next
        return result_list

    def generateLink(self, link_list: List):
        current = self.head = ListNode()
        for i in link_list:
            current.next = ListNode(i)
            current = current.next
