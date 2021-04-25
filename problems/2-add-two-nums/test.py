import unittest
from .siri import ListNode, Solution
from .wxp import twonumbers_sum

l1 = None
l2 = None
last_l1 = None
last_l2 = None

for i in [2, 4, 3]:
    temp = ListNode(i)
    if last_l1:
        last_l1.next = temp
    else:
        l1 = temp
    last_l1 = temp

for i in [5, 6, 4]:
    temp = ListNode(i)
    if last_l2:
        last_l2.next = temp
    else:
        l2 = temp
    last_l2 = temp


class TestStringMethods(unittest.TestCase):

    def test_siri(self):
        s = Solution()
        self.assertEqual(s.addTwoNumbers(l1, l2), 708)

    @unittest.skip('this method has an invalid input')
    def test_wxp(self):
        self.assertEqual(twonumbers_sum(l1, l2), 708)


if __name__ == '__main__':
    unittest.main()
