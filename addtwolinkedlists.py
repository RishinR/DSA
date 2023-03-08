# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        itr1 = l1
        itr2 = l2
        l3 = None
        itr3 = l3
        if itr1 is None:
            return itr2
        elif itr2 is None:
            return itr1
        carry = 0
        data = 0
        while itr1 and itr2:
            if l3 is None:
                data = itr1.val + itr2.val

                if data > 9:
                    carry = 1
                    l3 = ListNode(data-10, None)
                else:
                    l3 = ListNode(data, None)
                itr3 = l3
            else:
                data = itr1.val + itr2.val + carry
                if data > 9:
                    itr3.next = ListNode(data-10, None)
                    carry = 1
                else:
                    carry = 0
                    itr3.next = ListNode(data, None)
                itr3 = itr3.next
            itr1 = itr1.next
            itr2 = itr2.next
        while itr1:
            data = itr1.val+carry
            if data > 9:
                itr3.next = ListNode(data-10, None)
                carry = 1
            else:
                carry = 0
                itr3.next = ListNode(data, None)
            itr3 = itr3.next
            itr1 = itr1.next
        while itr2:
            data = itr2.val + carry
            if data > 9:
                itr3.next = ListNode(data-10, None)
                carry = 1
            else:
                carry = 0
                itr3.next = ListNode(data, None)
            itr3 = itr3.next
            itr2 = itr2.next
        if carry == 1:
            itr3.next = ListNode(1, None)
            itr3 = itr3.next
        return l3
