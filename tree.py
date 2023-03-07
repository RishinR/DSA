class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def addchild(self, child):
        child.parent = self
        self.children.append(child)
    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def printtree(self):
        spaces = " "*self.getlevel()*3
        
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.printtree()
def buildtree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.addchild(TreeNode("Mac"))
    laptop.addchild(TreeNode("Windows"))
    
    cellphone = TreeNode("Cellphone")
    cellphone.addchild(TreeNode("iphone"))
    cellphone.addchild(TreeNode("android"))
    
    root.addchild(laptop)
    root.addchild(cellphone)
    return root

if __name__ == "__main__":
    root = buildtree()
    root.printtree()