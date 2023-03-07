class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        lisstr = ""
        while itr:
            lisstr += str(itr.data) + "-->"    
            itr = itr.next
        print(lisstr)
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)
    def get_length(self):
        count  = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        print(count)
    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Not a valid index")
        if index == 0:
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1
    def insertat(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Not a valid index")
        elif index == 0:
            self.insert_at_begining(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
    def insert_after_val(self, value, newval):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(newval, itr.next)
                itr.next = node
                break
            itr = itr.next
    def removeval(self, value):
        itr = self.head
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next
if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_values([1, 2, 3, 4, 5])
    ll.get_length()
    ll.remove(2) #index 2 element needs to be removed
    ll.print()
    ll.insertat(2, 3)
    ll.insertat(3, "hala")
    ll.insert_after_val("hala", "madrid")
    ll.removeval("hala")
    ll.removeval("madrid")
    ll.print()