from Tree import TreeNode
from BinaryTree import BSTNode
class TestTree:
    def initialization():
        a = TreeNode("A")
        b = TreeNode("B")
        c = TreeNode("C")
        d = TreeNode("D")
        e = TreeNode("E")
        f = TreeNode("F")
        g = TreeNode("G")
        h = TreeNode("H")

        a.add_child(b)
        a.add_child(c)
        b.add_child(d)
        b.add_child(e)
        c.add_child(f)
        d.add_child(g)
        d.add_child(h)

        return a
    
    def test_remove_child(tree: TreeNode,target):
        tree.remove_child(target)
        print(f"The new tree is: {tree}")

    def test_tree_height(tree: TreeNode):
        height = tree.tree_height()
        print(f"The height of tree is: {height}")

    def test_find_level(tree: TreeNode, target):
        lvl = tree.find_level(target)
        print(f"The level of {target} is: {lvl}")

    def test_dfs(tree: TreeNode):
        lis = ",".join([node.value for node in tree.depth_first_traversal()])
        print(f"Depth first traversal the tree we have is: { lis }")

    def test_bfs(tree: TreeNode):
        print(f"Depth first traversal the tree we have is: {tree}")

class TestBSTree:
    def initialization():
        a = BSTNode(6)
        a.insert(5)
        a.insert(7)
        a.insert(8)
        a.insert(4)
        a.insert(3)
        a.insert(2)
        a.insert(100)
        a.insert(27)
        a.insert(18)
        return a
    
    def test_breadth_first_traversal(tree: BSTNode):
        print(f"Breadth first traversal for tree is: {tree}")

    def test_node_count(tree: BSTNode):
        print(f"Total node count of tree: {len(tree)}")

    def test_in_order_traversal(tree: BSTNode):
        str_tree = [str(i) for i in tree.in_order_traversal()]
        tree_string = ",".join(str_tree)
        print(f"In order traversal for tree is: {tree_string}")

    def test_pre_order_traversal(tree: BSTNode):
        str_tree = [str(i) for i in tree.pre_order_traversal()]
        tree_string = ",".join(str_tree)
        print(f"Pre order traversal for tree is: {tree_string}")

    def test_post_order_traversal(tree: BSTNode):
        str_tree = [str(i) for i in tree.post_order_traversal()]
        tree_string = ",".join(str_tree)
        print(f"Post order traversal for tree is: {tree_string}")

    def test_search(tree:BSTNode, target):
        if tree.search(target) == True:
            print(f"{target} is in the tree")
        else:
            print(f"{target} is not in the tree")

    def test_get_min(tree: BSTNode):
        print(f"{tree.get_min()} is minimum in the tree")

    def test_get_max(tree: BSTNode):
        print(f"{tree.get_max()} is maximum in the tree")

    def test_height(tree: BSTNode):
        print(f"{tree.get_height()} is the height of the tree")

    def test_delete_node(tree: BSTNode, value):
        tree.delete_node(value)
        print(f"Breadth first traversal for new tree after remove {value} is: {tree}")

    def test_get_successor(tree: BSTNode, value):
        print(f"Successor of {value} is: {tree.get_successor(value)}")

    def test_is_binary_search_tree(tree: BSTNode):
        print(f"The tree is BST is:{tree.is_binary_search_tree()}")
    
    def test_delete_tree(tree:BSTNode):
        tree.delete_tree
        print(f"Deleted tree: {tree}")

    
def testTree():
    a = TestTree.initialization()
    print(a)
    TestTree.test_remove_child(a,"G")
    TestTree.test_tree_height(a)
    TestTree.test_find_level(a,"D")
    TestTree.test_dfs(a)
    TestTree.test_bfs(a)
    

def testBST():
    b = TestBSTree.initialization()
    TestBSTree.test_breadth_first_traversal(b)
    TestBSTree.test_node_count(b)
    TestBSTree.test_in_order_traversal(b)
    TestBSTree.test_pre_order_traversal(b)
    TestBSTree.test_post_order_traversal(b)
    TestBSTree.test_search(b, 2)
    TestBSTree.test_search(b, 69)
    TestBSTree.test_get_max(b)
    TestBSTree.test_get_min(b)
    TestBSTree.test_delete_node(b, 5)
    TestBSTree.test_get_successor(b, 7)
    TestBSTree.test_is_binary_search_tree(b)

    

if __name__ == "__main__":

    
    testBST()