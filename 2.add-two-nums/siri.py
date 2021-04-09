# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printNode(self):
      print(self.val)
      if self.next != None:
        self.next.printNode()

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
      head = result = ListNode()
      carry = 0
      while l1 != None or l2 != None:
        if l1 != None:
          l1_num = l1.val
          l1 = l1.next
        else:
          l1_num = 0

        if l2 != None:
          l2_num = l2.val
          l2 = l2.next
        else:
          l2_num = 0

        temp = l1_num + l2_num + carry
        carry = int(temp / 10)
        result.val = temp % 10
        if l1 != None or l2 != None:
          result.next = ListNode()
          result = result.next
        else:
          return head


l1 = None
l2 = None

last_l1 = None
last_l2 = None

for i in [2,4,3]:
  temp = ListNode(i)
  if last_l1:
    last_l1.next = temp
  else:
    l1 = temp
  last_l1 = temp

for i in [5,6,4]:
  temp = ListNode(i)
  if last_l2:
    last_l2.next = temp
  else:
    l2 = temp
  last_l2 = temp

s = Solution()
result = s.addTwoNumbers(l1, l2)
result.printNode()
