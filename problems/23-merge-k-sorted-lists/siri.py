from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    total_count = 0

    def mergeKLists(self, lists: List[ListNode]):
        self.total_count = 0
        links = []
        for l in lists:
            links.append(self.generateLink(l).next)
        count = 0
        head = current = ListNode()
        while self.total_count != count:
            count += 1
            smallest = None
            for i in range(len(links)):
                if links[i] == None:
                    continue
                if smallest == None:
                    smallest = i
                    continue
                if links[i].val < links[smallest].val:
                    smallest = i
            current.next = links[smallest]
            links[smallest] = links[smallest].next
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
            self.total_count += 1
            current = current.next
        return head
