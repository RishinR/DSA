class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
if __name__ == "__main__":
    list1 = ListNode() # head
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8]
    itr = list1
    count = 0
    for i in l1:
        node = ListNode(i, None)
        if count == 0:
            list1 = node
            count += 1
        else:
            itr.next = node
            itr = itr.next
        
    itr = list1
    liststr = ""
    while itr:
        liststr += str(itr.val) + "-->"
        itr = itr.next
    print(liststr)