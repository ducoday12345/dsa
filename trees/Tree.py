class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []
 
    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, target):
        self.children = [child for child in self.children if child.value != target]

    def tree_height(self):
        if not self.children: # leaves node
            return 1
        return 1 + max(child.tree_height() for child in self.children)
    
    def find_level(self, target, current_lvl = 0):
        if self.value == target:
            return current_lvl
        for i in self.children:
            level = i.find_level(target, current_lvl+1)
            if level != None:
                return level
        return None
    
    def breadth_first_traversal(self):
        queue = [self]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node)
            queue += node.children
        return res
    
    def depth_first_traversal(self):
        stack = [self]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            stack += node.children.reverse()
        return res
    
    #print in form of bfs
    def __str__(self):
        return ",".join(self.breadth_first_traversal())