from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, lists: List[int]):
        head = prev = self.generateLink(lists)
        current = prev.next
        while current != None:
            if current.next == None:
                break
            temp_node = current.next
            current.next = current.next.next
            temp_node.next = current
            prev.next = temp_node
            prev = current
            current = current.next

        result = []
        head = head.next
        while head != None:
            result.append(head.val)
            head = head.next
        return result

    def generateLink(self, l: List):
        head = current = ListNode()
        for i in l:
            current.next = ListNode(i)
            current = current.next
        return head
