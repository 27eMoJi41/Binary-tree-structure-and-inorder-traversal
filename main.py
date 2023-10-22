class Node:
    def __init__(self,val) :
            self.data = val
            self.left = None
            self.right = None

    def inorder_traversal(self):
        
        if self.left:
                self.left.inorder_traversal()

        print(self.data,end=" ")

        if self.right:
                self.right.inorder_traversal()
              
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.inorder_traversal()
    
        