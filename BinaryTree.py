import random

class Node():
    def __init__(self,value):
        self.value = value
        self.left  = None
        self.right = None

    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right

    def getvalue(self):
        return self.value

class BinaryTree():
    def __init__(self,ListIn,idx):
        if len(ListIn)==0:
            self = None
        else:
            if idx<len(ListIn):
                self.Root = Node(ListIn[idx])
                self.createTree(ListIn)
            else:
                self = None
    def createTree(self,ListIn):

        for i in range(0,len(ListIn)):
            node = self.Root
            value = ListIn[i]
            self.Insert(node,value)
            
    def Insert(self,node,value):        
        if value<node.getvalue():
            if not node.getleft():
                node.left = Node(value)
            else:
                
                self.Insert(node.left,value)
        elif value>node.getvalue():
            if not node.getright():
                node.right = Node(value)
            else:
                self.Insert(node.right,value)

    def PreOrderTraverse(self,root):
 
        print(root.getvalue())
        if root.getleft():
            self.PreOrderTraverse(root.getleft())
        if root.getright():
            self.PreOrderTraverse(root.getright())

    def InOrderTraverse(self,root):
        
        if root.getleft():
            self.PreOrderTraverse(root.getleft())
        print(root.getvalue())
        if root.getright():
            self.PreOrderTraverse(root.getright())
            
    def PostOrderTraverse(self,root):
        
        if root.getleft():
            self.PreOrderTraverse(root.getleft())
        if root.getright():
            self.PreOrderTraverse(root.getright())
        print(root.getvalue())

if __name__=="__main__":
    List = [random.randint(1,20) for i in range(10)]
    ListIn = set(List)
    ListIn = list(ListIn)
    #ListIn = [3, 6, 8, 11, 16, 19, 20]
    BT = BinaryTree(ListIn,4)
    BT.InOrderTraverse(BT.Root)
