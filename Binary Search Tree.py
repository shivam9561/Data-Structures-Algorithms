class node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None
class bst:
    def createnode(self,data):
        return node(data)
    def insert_node(self,root,new_node):
        if root is None:
            return self.createnode(new_node)
        if new_node < root.data:
            root.left = self.insert_node(root.left,new_node)
        elif new_node > root.data:
            root.right = self.insert_node(root.right,new_node)
        return root
    
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
    

    def preorder(self, root):
        if root is not None:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

tree = bst()    
root = tree.createnode(5)
tree.insert_node(root,10)
tree.insert_node(root,3)
tree.insert_node(root,2)
tree.insert_node(root,1)
tree.insert_node(root,15)
tree.insert_node(root,20)
tree.preorder(root)
tree.inorder(root)
print
 