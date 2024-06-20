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
    def preorder(self,root):
        if root :
            print(root.data,end="->")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root :
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.data,end="->")
        
    
t1=tree()
t1.insert(t1.root,10)
t1.insert(t1.root,5)
t1.insert(t1.root,1)
t1.insert(t1.root,7)
t1.insert(t1.root,6)
t1.insert(t1.root,8)
t1.insert(t1.root,20)
t1.insert(t1.root,25)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()