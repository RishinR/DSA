class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
    def print(self):
        itr = self.head
        lisstr = ""
        while itr:
            lisstr += str(itr.data) + "-->"
            itr = itr.next
        print(lisstr)
    def reverse(self):
        if self.head is None:
            return self.head
        else:
            prev = None
            curr = self.head
            
        while curr:
            next_node = curr.next # next element after head
            curr.next = prev # head.next = None
            prev = curr # setting new prev as current value fro next iteration
            curr = next_node # setting current as next_node  
        self.head = prev      
if __name__ == "__main__":
    l = LinkedList()

    for i in range(0, 5):
        n = int(input("Enter a number: "))
        l.insert(n)
    l.reverse()
    l.print()