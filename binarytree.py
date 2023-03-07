class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def addchild(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addchild(data)
            else:
                self.left = node(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = node(data)
    def inorder(self):
        l = []
        # visit left subtree
        if self.left:
            l += self.left.inorder()
        # visit base node
        l.append(self.data)
        # visit right subtree 
        if self.right:
            l += self.right.inorder()
        return l
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False
def maxdepth(root):
    if root == None:
        return 0
    
    leftdepth = maxdepth(root.left)
    rightdepth = maxdepth(root.right)
    
    return(max(leftdepth+1, rightdepth + 1))
            
def buildtree(l):
    root = node(l[0])
    for i in range(0, len(l)):
        root.addchild(l[i])
    return root

if __name__ == "__main__":
    l = [5, 1, 3, 7, 2, 0, 6, 8, 4]
    root = buildtree(l)
    print(root.inorder()) # will be done in log(n) time complexity
    s = root.search(25)
    print(s)
    print(maxdepth(root))
