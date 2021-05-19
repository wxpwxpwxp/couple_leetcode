# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        print(self.val)
        if self.next is not None:
            self.next.printNode()


class Solution:
    def getResult(self, head):
        s = ''
        while(head is not None):
            s += str(head.val)
            head = head.next
        return int(s)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        head = result = ListNode()
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_num = l1.val
                l1 = l1.next
            else:
                l1_num = 0

            if l2 is not None:
                l2_num = l2.val
                l2 = l2.next
            else:
                l2_num = 0

            temp = l1_num + l2_num + carry
            carry = int(temp / 10)
            result.val = temp % 10
            if l1 is not None or l2 is not None:
                result.next = ListNode()
                result = result.next
            else:
                return self.getResult(head)
