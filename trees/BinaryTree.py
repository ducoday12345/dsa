class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None #Node left
        self.right = None #Node right

    def insert(self, value):
        if self.value == value:
            return
            # raise Exception("Value is already in Tree") 
        if value < self.value:
            if self.left:
                self.left.insert(value) # recursively insert value to left node
            else:
                self.left = BSTNode(value)

        else:
            if self.right:
                self.right.insert(value) # recursively insert value to right node
            else:
                self.right = BSTNode(value)

    def breadth_first_traversal(self): #level order traversal
        visited = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            visited.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return visited

    def __str__(self):
        return ",".join(str(i) for i in self.breadth_first_traversal())
    
    def __len__(self):
        return self.get_node_count()

    def get_node_count(self):
        left_count = len(self.left) if self.left else 0
        right_count = len(self.right) if self.right else 0
        return left_count + right_count +1
    
    def in_order_traversal(self):
        result = []
        if self.left:
            result += self.left.in_order_traversal()
        result.append(self.value)
        if self.right:
            result += self.right.in_order_traversal()
        return result
    
    def search(self, value):
        if self.value == value:
            return True
        elif self.left and self.value > value:
            return self.left.search(value)
        elif self.right and self.value < value:
            return self.right.search(value)
        return False




    
