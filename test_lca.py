import unittest
import lca


class test_lca(unittest.TestCase):

    #test a simple tree/base case
    def test_basicTree(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        self.assertEqual(2, lca.lowestCommonAncestor(root, 4, 5))

    #test on an empty tree expect error
    def test_nullTree(self):
        root = None
        self.assertEqual(-1, lca.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')

    #test for a node which is not contained in the tree
    def test_InvalidNode(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        self.assertEqual(-1, lca.lowestCommonAncestor(root, 4, 8), "Unfound node returns -1")

    #test for case when the common ancestor is one of the query nodes
    def test_commonAncestorIsNode(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        self.assertEqual(2, lca.lowestCommonAncestor(root, 2, 4), "Common Ancestor of 2 & 4 is 2 itself")
        self.assertEqual(2, lca.lowestCommonAncestor(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
        self.assertEqual(2, lca.lowestCommonAncestor(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")

        ## TODO: add more edge case tests as i think of exceptional circuimstances


if __name__ == '__main__':
    unittest.main()
