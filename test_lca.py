import unittest
import lca


class test_lca(unittest.TestCase):

    def test_basicTree(self):
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.left.right = Node(5) 
        root.right.left = Node(6) 
        root.right.right = Node(7) 
        self.assertEquals(lowestCommonAncestor(root, 4, 5), 2)

if __name__ == '__main__':
    unittest.main()
# Driver program to test above function 
# Let's create the Binary Tree shown in above diagram 
#root = Node(1) 
#root.left = Node(2) 
#root.right = Node(3) 
#root.left.left = Node(4) 
#root.left.right = Node(5) 
#root.right.left = Node(6) 
#root.right.right = Node(7) 
  
#print ("LCA(4, 5) = %d" %(lowestCommonAncestor(root, 4, 5))) 
#print ("LCA(4, 6) = %d" %(lowestCommonAncestor(root, 4, 6))) 
#print ("LCA(3, 4) = %d" %(lowestCommonAncestor(root,3,4))) 
#print ("LCA(2, 4) = %d" %(lowestCommonAncestor(root,2, 4))) 