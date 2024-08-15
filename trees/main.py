from Tree import TreeNode
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

if __name__ == "__main__":
    a = TestTree.initialization()
    print(a)
    TestTree.test_remove_child(a,"G")
    TestTree.test_tree_height(a)
    TestTree.test_find_level(a,"D")
    TestTree.test_dfs(a)
    TestTree.test_bfs(a)
