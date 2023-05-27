# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        itr1 = head
        if head.next == None:
            return head
        itr2 = head.next
        if head.next.next == None:
            itr2.next = itr1
            itr1.next = None
            head = itr2
            return head
        itr3 = head.next.next

        while itr3:
            if itr1 == head:
                itr1.next = None
            itr2.next = itr1
            itr1 = itr2
            itr2 = itr3
            itr3 = itr3.next
        itr2.next = itr1
        head = itr2
        return head
