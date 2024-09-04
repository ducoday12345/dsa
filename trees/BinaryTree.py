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
    
    def search(self, value):
        if self.value == value:
            return True
        elif self.left and self.value > value:
            return self.left.search(value)
        elif self.right and self.value < value:
            return self.right.search(value)
        return False
    
    def find(self, value):
        if self.value == value:
            return self
        elif self.left and self.value > value:
            return self.left.find(value)
        elif self.right and self.value < value:
            return self.right.find(value)
        return None

    def pre_order_traversal(self):
        result = []
        result.append(self.value)
        if self.left:
            result += self.left.pre_order_traversal()
        if self.right:
            result += self.right.pre_order_traversal()
        return result

    def post_order_traversal(self):
        result = []
        if self.left:
            result += self.left.post_order_traversal()
        if self.right:
            result += self.right.post_order_traversal()
        result.append(self.value)
        return result

    def delete_tree(self):
        self.left = None
        self.right = None
        self.value = None

    def get_min(self):
        current = self
        while current.left :
            current = current.left
        return current.value
    
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value
    
    def get_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return max(left_height, right_height)+1
    
    def delete_node(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete_node(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete_node(value)
        else:
            if not self.left: 
                return self.right
            if not self.right: 
                return self.left
            min_larger_value = self.right.get_min()
            self.value = min_larger_value
            
            self.right = self.right.delete_node(min_larger_value)
        
        return self


    def get_successor(self, value):
        node = self.find(value)
        
        if not node:
            return None
        if node.right:
            return node.right.get_min()
        successor = None
        current = self
        while current:
            if value < current.value:
                successor = current
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                break
        return successor.value if successor else None

    
    def is_binary_search_tree(self, min_value=float('-inf'), max_value=float('inf')):
        if not (min_value < self.value < max_value):
            return False
    
        left_is_bst = self.left.is_binary_search_tree(min_value, self.value) if self.left else True
        
        right_is_bst = self.right.is_binary_search_tree(self.value, max_value) if self.right else True
        
        return left_is_bst and right_is_bst
    

    
