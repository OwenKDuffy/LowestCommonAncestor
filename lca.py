class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val =  val
        self.children = []
        self.ancestors = []
        self.maxDepth = 0;
                                                    #graph is no longer binary tree so could have more than two children

    def addChild(self, n):
        self.children.append(n)                     #give this node new child n
        n.ancestors.extend(self.ancestors)          #give n all of this nodes ancestors
        n.ancestors.append(self)                    #add this node as an ancestor of n's
        if n.maxDepth < self.maxDepth + 1:
            n.maxDepth = self.maxDepth + 1          #if this Node is the deepest ancestor of n make n one deeper

    def printAncestors(self):
        print ("Ancestors of", self.val)
        for x in self.ancestors:
            print ("Parent = " , x.val , ", Depth = " , x.maxDepth , "\n")


def lowestCommonAncestor(root, x, y):
    if root == None:                                 #there is no tree return error
        return -1


    # find two nodes
    n1 = findNode(root, x)
    n2 = findNode(root, y)


    if n1 == n2:
        return n1.val                               #LCA of same node is itself


    if n1 == None or n2 == None:                    #error no such node exists
        return -1


    deepestAncestorDepth = -1
    deepestAncestor = None
    for i in n1.ancestors:
        if i in n2.ancestors:
            if i.maxDepth > deepestAncestorDepth:
                deepestAncestor = i
                deepestAncestorDepth = i.maxDepth

    #check if node itself is not an ancestor
    if n1 in n2.ancestors:                          #if n1 is an ancestor of n2
        if n1.maxDepth > deepestAncestorDepth:      #and if n1 is deeper than previous deepest ancestor
            deepestAncestor = n1
            deepestAncestorDepth = n1.maxDepth

    #vice versa
    if n2 in n1.ancestors:                         #if n2 is an ancestor of n1
        if n2.maxDepth > deepestAncestorDepth:     #and if n2 is deeper than previous deepest ancestor
            deepestAncestor = n2
            deepestAncestorDepth = n2.maxDepth



    return deepestAncestor.val


def findNode(node, val):
    if node.val == val:
        return node
    elif len(node.children) != 0:
        for x in node.children:
            n = findNode(x, val)
            if n != None:
                return n
    else:
        return None
