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
