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

if __name__ == "__main__":
    a = TestTree.initialization()
    print(a)
