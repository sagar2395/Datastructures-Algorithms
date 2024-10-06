class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0
        
    def insert(self, data):
        new_node = Node(data)
        
        if self.root == None:
            self.root = Node
            self.number_of_nodes = 1
            return
        else:
            current_node = self.root
            
        
        