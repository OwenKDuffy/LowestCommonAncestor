import unittest
import lca

def createBinaryTreeStyleGraph():
    root = lca.Node(1)
    n2 = lca.Node(2)
    n3 = lca.Node(3)
    n4 = lca.Node(4)
    n5 = lca.Node(5)
    n6 = lca.Node(6)
    n7 = lca.Node(7)
    root.addChild(n2)
    root.addChild(n3)
    n2.addChild(n4)
    n2.addChild(n5)
    n3.addChild(n6)
    n3.addChild(n7)
    return root


def createADG():
    root = lca.Node(1)
    n2 = lca.Node(2)
    n3 = lca.Node(3)
    n4 = lca.Node(4)
    n5 = lca.Node(5)
    n6 = lca.Node(6)
    n7 = lca.Node(7)
    n8 = lca.Node(8)
    n9 = lca.Node(9)
    n10 = lca.Node(10)
    n11 = lca.Node(11)
    n12 = lca.Node(12)
    n13 = lca.Node(13)
    n14 = lca.Node(14)
    root.addChild(n2)
    root.addChild(n3)
    n2.addChild(n5)
    n2.addChild(n4)
    n3.addChild(n4)
    n3.addChild(n7)
    n4.addChild(n11)
    n4.addChild(n6)
    n5.addChild(n8)
    n6.addChild(n10)
    n6.addChild(n13)
    n7.addChild(n9)
    n8.addChild(n10)
    n9.addChild(n12)
    n10.addChild(n14)
    n11.addChild(n10)
    n13.addChild(n12)
    n13.addChild(n14)
    return root

class test_lca(unittest.TestCase):

    #Housekeeping, these functions make the tests neater to look at



    # test a simple binary tree/base case
    def test_basicTree(self):
        root = createBinaryTreeStyleGraph()
        self.assertEqual(2, lca.lowestCommonAncestor(root, 4, 5))
        self.assertEqual(1, lca.lowestCommonAncestor(root, 4, 6))



    #test on an empty tree expect error
    def test_nullTree(self):
        root = None
        self.assertEqual(-1, lca.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')

    #test for a node which is not contained in the tree
    def test_InvalidNode(self):
        root = createBinaryTreeStyleGraph()
        self.assertEqual(-1, lca.lowestCommonAncestor(root, 4, 8), "Unfound node returns -1")

    #test for case when the common ancestor is one of the query nodes
    def test_commonAncestorIsNode(self):
        root = createBinaryTreeStyleGraph()
        self.assertEqual(2, lca.lowestCommonAncestor(root, 2, 4), "Common Ancestor of 2 & 4 is 2")
        self.assertEqual(2, lca.lowestCommonAncestor(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
        self.assertEqual(2, lca.lowestCommonAncestor(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")

    def test_simpleTree(self):
        n4 = lca.Node(4)
        n11 = lca.Node(11)
        n6 = lca.Node(6)
        n4.addChild(n11)
        n4.addChild(n6)
        self.assertEqual(4, lca.lowestCommonAncestor(n4, 11, 6), "Common Ancestor of 11 & 6 is 4")


    def test_multipleRoutes(self):
        root = createADG()
        # lca.findNode(root, 10).printAncestors() these were for debugging
        # lca.findNode(root, 12).printAncestors()
        self.assertEqual(6, lca.lowestCommonAncestor(root, 10, 12), "Common Ancestor of 10 & 12 is 6")
        self.assertEqual(2, lca.lowestCommonAncestor(root, 8, 13), "Common Ancestor of 8 & 13 is 2")
        self.assertEqual(3, lca.lowestCommonAncestor(root, 6, 9), "Common Ancestor of 6 & 9 is 3")

        ## TODO: add more edge case tests as i think of exceptional circuimstances






if __name__ == '__main__':
    unittest.main()
