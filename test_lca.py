import unittest
import lca


class test_lca(unittest.TestCase):

    def test_basicTree(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)
        self.assertEqual(lca.lowestCommonAncestor(root, 4, 5), 2)

if __name__ == '__main__':
    unittest.main()
# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
#root = lca.Node(1)
#root.left = lca.Node(2)
#root.right = lca.Node(3)
#root.left.left = lca.Node(4)
#root.left.right = lca.Node(5)
#root.right.left = lca.Node(6)
#root.right.right = lca.Node(7)

#print ("LCA(4, 5) = %d" %(lowestCommonAncestor(root, 4, 5)))
#print ("LCA(4, 6) = %d" %(lowestCommonAncestor(root, 4, 6)))
#print ("LCA(3, 4) = %d" %(lowestCommonAncestor(root,3,4)))
#print ("LCA(2, 4) = %d" %(lowestCommonAncestor(root,2, 4)))
