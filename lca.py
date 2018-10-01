class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val =  val
        self.left = None
        self.right = None

def lowestCommonAncestor(root, x, y):
    
    #create paths
    path1 = []
    path2 = []

    if (not findPath(root, path1, x) or not findPath(root, path2, y)):
        return -1


    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  

def findPath( root, path, k): 
  
    # Baes Case 
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.val) 
  
    # See if the k is same as root's val 
    if root.val == k : 
        return True
  
    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove 
    # root from path and return False 
       
    path.pop() 
    return False
  

