from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, lists: List[int], k: int):
        head = prev = self.generateLink(lists)
        current = prev.next
        while current != None:
            node_list = []
            end = False
            for i in range(k):
                if current == None:
                    end = True
                    break
                temp_node = current.next
                current.next = None
                node_list.append(current)
                current = temp_node

            if end:
                for i in range(len(node_list)):
                    prev.next = node_list[i]
                    prev = prev.next
            else:
                for i in range(len(node_list)):
                    prev.next = node_list.pop()
                    prev = prev.next

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
