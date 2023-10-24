from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_vector(root):
    vector = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            vector.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return vector

root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(None)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(None)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(None)

root2 = TreeNode(50)
root2.left = TreeNode(17)
root2.right = TreeNode(76)
root2.left.left = TreeNode(9)
root2.left.right = TreeNode(23)
root2.right.left = TreeNode(54)
root2.right.right = TreeNode(None)
root2.left.left.left = TreeNode(None)
root2.left.left.right = TreeNode(14)
root2.left.right.left = TreeNode(19)
root2.left.right.right = TreeNode(None)
root2.right.left.left = TreeNode(None)
root2.right.left.right = TreeNode(72)
root2.left.left.right.left = TreeNode(12)
root2.left.left.right.right = TreeNode(None)
root2.right.left.right.left = TreeNode(67)
root2.right.left.right.right = TreeNode(None)



# Vector 1
vector = tree_to_vector(root)
print(vector)

level_start = 0
level_end = 1
while level_start < len(vector):
    print(vector[level_start:level_end])
    level_start = level_end
    level_end += 2**(level_end.bit_length() - 1)

# Vector 2
vector2 = tree_to_vector(root2)
print(vector2)
level_start = 0
level_end = 1
while level_start < len(vector2):
    print(vector2[level_start:level_end])
    level_start = level_end
    level_end += 2**(level_end.bit_length() - 1)

# Bài 2
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create the tree 1
root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(None)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(None)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(None)

# create the tree 2
root2 = TreeNode(50)
root2.left = TreeNode(17)
root2.right = TreeNode(76)
root2.left.left = TreeNode(9)
root2.left.right = TreeNode(23)
root2.right.left = TreeNode(54)
root2.right.right = TreeNode(None)
root2.left.left.left = TreeNode(None)
root2.left.left.right = TreeNode(14)
root2.left.right.left = TreeNode(19)
root2.left.right.right = TreeNode(None)
root2.right.left.left = TreeNode(None)
root2.right.left.right = TreeNode(72)
root2.left.left.right.left = TreeNode(12)
root2.left.left.right.right = TreeNode(None)
root2.right.left.right.left = TreeNode(67)
root2.right.left.right.right = TreeNode(None)

def traverse(node):
    if node:
        print(node.val)
        traverse(node.left)
        traverse(node.right)

# traverse the first tree
print("First tree:")
traverse(root)

# traverse the second tree
print("Second tree:")
traverse(root2)

# Bài 3
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# create the tree 1
root = TreeNode(2)
root.left = TreeNode(7)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(None)
root.right.right = TreeNode(9)
root.left.left.left = TreeNode(None)
root.left.right.left = TreeNode(5)
root.left.right.right = TreeNode(11)
root.right.right.left = TreeNode(4)
root.right.right.right = TreeNode(None)

# create the tree 2
root2 = TreeNode(50)
root2.left = TreeNode(17)
root2.right = TreeNode(76)
root2.left.left = TreeNode(9)
root2.left.right = TreeNode(23)
root2.right.left = TreeNode(54)
root2.right.right = TreeNode(None)
root2.left.left.left = TreeNode(None)
root2.left.left.right = TreeNode(14)
root2.left.right.left = TreeNode(19)
root2.left.right.right = TreeNode(None)
root2.right.left.left = TreeNode(None)
root2.right.left.right = TreeNode(72)
root2.left.left.right.left = TreeNode(12)
root2.left.left.right.right = TreeNode(None)
root2.right.left.right.left = TreeNode(67)
root2.right.left.right.right = TreeNode(None)

def NLR(node):
    if node:
        print(node.val, end=" ")
        NLR(node.left)
        NLR(node.right)

def LNR(node):
    if node:
        LNR(node.left)
        print(node.val, end=" ")
        LNR(node.right)

def LRN(node):
    if node:
        LRN(node.left)
        LRN(node.right)
        print(node.val, end=" ")

print("First tree:")
print("Pre-order traversal (NLR):", end=" ")
NLR(root)
print()
print("In-order traversal (LNR):", end=" ")
LNR(root)
print()
print("Post-order traversal (LRN):", end=" ")
LRN(root)
print()

# print the pre-order, in-order, and post-order traversals for the second tree
print("Second tree:")
print("Pre-order traversal (NLR):", end=" ")
NLR(root2)
print()
print("In-order traversal (LNR):", end=" ")
LNR(root2)
print()
print("Post-order traversal (LRN):", end=" ")
LRN(root2)
print()