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
            self.root = new_node
            self.number_of_nodes = 1
            return
        else:
            current_node = self.root 
            while(current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return
        
    def BFS(self):
        current_node = self.root
        if current_node is None:
            return "tree is empty"
        else:
            BFS_result = []
            queue = []
            queue.append(current_node)
            
            while(len(queue) > 0):
                current_node = queue.pop()
                BFS_result.append(current_node.data)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return BFS_result
        