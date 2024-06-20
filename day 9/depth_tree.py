class node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self,root,x):
        if self.root is None:
            self.root=node(x)
            return self.root
        if root==None:
            return node(x)
        elif root.data>x:
            root.left=self.insert(root.left,x)
        else:
           root.right=self.insert(root.right,x)
        return root
           
           
    def inorder(self,root):
        if root :
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    def search(self,root,x):
        if root is None:
            return False
        if root.data==x:
            return True
        elif x<root.data:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    def depth(self,root,x,c=0):
        if root is None:
            return -1
        if root.data==x:
            return c
        elif x<root.data:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
        
        
        
        
t1=tree()
t1.insert(t1.root,10)
t1.insert(t1.root,5)
t1.insert(t1.root,20)
t1.insert(t1.root,2)
t1.insert(t1.root,7)
t1.inorder(t1.root)
print()
print(t1.search(t1.root,20))
print(t1.depth(t1.root,20))


    







