class Node:
    def __init__(self, key = None, value = None):
        if key == None:
            self.left = None
            self.right = None
        else:
            l = Node()
            r = Node()
            self.left = l
            self.right = r
            l.setParent(self)
            r.setParent(self)
        self.key = key
        self.value = value
        self.parent = None
        self.color = "Black"
        self.looking = False
    def setParent(self, v):
        self.parent = v
    def setLeftChild(self, v):
        self.left = v
    def setRightChild(self,v):
        self.right = v
    def isRoot(self):
        if self.parent == None:
            return True
        else:
            return False
    def isLeaf(self):
        if self.left.getKey() == None and self.right.getKey() == None:
            return True
        else:
            return False
    def hasLeftChild(self):
        if self.left.getKey() != None:
            return True
        else:
            return False
    def hasRightChild(self):
        if self.right.getKey() != None:
            return True
        else:
            return False
    def getParent(self):
        return self.parent
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def getUncle(self):
        if self.isRoot():
            return None
        elif self.getParent().getKey() > self.getKey():
            return self.getParent().getRightChild()
        else:
            return self.getParent().getLeftChild()
    def deleteParent(self):
        self.parent = None
    def deleteLeftChild(self):
        l = Node()
        self.left = l
        l.setParent(self)
    def deleteRightChild(self):
        r = Node()
        self.right = r
        r.setParent(self)
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setKey(self, key):
        self.key = key
    def setValue(self, value):
        self.value = value
    def getKey(self):
        return self.key
    def getValue(self):
        return self.value
    def isLeftChild(self):
        if self.isRoot():
            return False
        if self.getParent().getLeftChild() == self:
            return True
        else:
            return False
    def isRightChild(self):
        if self.isRoot():
            return False
        if self.getParent().getRightChild() == self:
            return True
        else:
            return False
    def print(self):
        print(str(self.key) + " " + str(self.value))

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def find(self, key):
        if self.isEmpty():
            return
        current = self.root
        while current.getKey() != key and current.getKey() != None:
            if current.getKey() > key:
                current = current.getLeftChild()
            elif current.getKey() < key:
                current = current.getRightChild()
        return current
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    def insert(self, v):
        if self.isEmpty():
            self.root = v
            self.size += 1
        else:
            n = self.find(v.getKey())
            if n.getKey() != None:
                return
            elif v.getKey() < n.getParent().getKey():
                n.getParent().setLeftChild(v)
            else:
                n.getParent().setRightChild(v)
            self.size += 1
            v.setParent(n.getParent())
            del n
        self.insertCase(v)
    def remove(self, key):
        if self.isEmpty():
            return
        n = self.find(key)
        if n.getKey() == None:
            return
        if n.isRoot():
            self.root = None
            self.size -= 1
            del n
            return
        if n.isLeaf() == False:
            if n.hasLeftChild():
                current = n.getLeftChild()
                if current.hasRightChild():
                    while current.hasRightChild():
                        current = current.getRightChild()
                    current.getParent().setRightChild(current.getLeftChild())
                else:
                    n.setLeftChild(current.getLeftChild())
                del current.rught
                current.getLeftChild().setParent(current.getParent())
            else:
                current = n.getRightChild()
                if current.hasLeftChild():
                    while current.hasLeftChild():
                        current = current.getLeftChild()
                    current.getParent().setLeftChild(current.getRightChild())
                else:
                    n.setRightChild(current.getRightChild())
                del current.left
                current.getRightChild().setParent(current.getParent())
            n.setKey(current.getKey())
            n.setValue(current.getValue())
            del current
        else:
            if n.getParent().getKey() > n.getKey():
                n.getParent().deleteLeftChild()
            else:
                n.getParent().deleteRightChild()
            del n.left
            del n.right
            del n
        self.size -= 1
    def insertCase(self, current):
        if current.isRoot():
            current.setColor("Black")
        elif current.getParent().getColor() == "Black":
            current.setColor("Red")
        elif current.getParent().getColor() == "Red":
            if current.getParent().getUncle().getColor() == "Red":
                current.setColor("Red")
                current.getParent().setColor("Black")
                current.getParent().getUncle().setColor("Black")
                current.getParent().getParent().setColor("Red")
                self.insertCase(current.getParent().getParent())
            else:
                if current.isLeftChild() != current.getParent().isLeftChild():
                    if current.isLeftChild():
                        current.getParent().getParent().setRightChild(current)
                        current.getParent().setLeftChild(current.getRightChild())
                        current.getRightChild().setParent(current.getParent())
                        current.setRightChild(current.getParent())
                        current.setParent(current.getParent().getParent())
                        current.getRightChild().setParent(current)
                        current = current.getRightChild()
                    else:
                        current.getParent().getParent().setLeftChild(current)
                        current.getParent().setRightChild(current.getLeftChild())
                        current.getLeftChild().setParent(current.getParent())
                        current.setLeftChild(current.getParent())
                        current.setParent(current.getParent().getParent())
                        current.getLeftChild().setParent(current)
                        current = current.getLeftChild()
                current.setColor("Red")
                current = current.getParent()
                if current.getParent().isRoot():
                    self.root = current
                current.setColor("Black")
                current.getParent().setColor("Red")
                if current.isLeftChild():
                    current.getParent().setLeftChild(current.getRightChild())
                    current.getRightChild().setParent(current.getParent())
                    if current.getParent().isLeftChild():
                        current.getParent().getParent().setLeftChild(current)
                    elif current.getParent().isRightChild():
                        current.getParent().getParent().setRightChild(current)
                    current.setRightChild(current.getParent())
                    current.setParent(current.getParent().getParent())
                    current.getRightChild().setParent(current)
                else:
                    current.getParent().setRightChild(current.getLeftChild())
                    current.getLeftChild().setParent(current.getParent())
                    if current.getParent().isLeftChild():
                        current.getParent().getParent().setLeftChild(current)
                    elif current.getParent().isRightChild():
                        current.getParent().getParent().setRightChild(current)
                    current.setLeftChild(current.getParent())
                    current.setParent(current.getParent().getParent())
                    current.getLeftChild().setParent(current)




    def printInOrder(self, current = None):
        if current == None:
            current = self.root
        if current.getKey() != None:
            self.printInOrder(current.getLeftChild())
            current.print()
            self.printInOrder(current.getRightChild())

def main():
    v1 = Node(1, "kenny")
    print(v1.isRoot())
    print(v1.isLeaf())
    v1.print()
    T = RedBlackTree()
    T.insert(v1)
    T.insert(Node(2, "j"))
    T.insert(Node(1.5, "k"))
    T.insert(Node(0.7, "s"))
    T.insert(Node(2.2, "h"))
    T.insert(Node(1.8, "a"))
    T.remove(2)
    T.printInOrder()

if __name__ == '__main__':
    main()
