"""
### - Assignment 3
Amy Brons - 20252295

This assignment contains a non-recursive in-order
tree walk algorithm. For this project I have decided to that
the algorithm will use a stack as an auxillary data structure.
"""

from collections import deque # import stack lib

"""
Class of node is created to draw the tree onto, and traverse
through the nodes.
"""
class Node:
    def __init__(self,data = None, left = None, right = None):
        self.data = data # initializing the node data
        self.left = left 
        self.right = right
        
"""
Function to walk the binary code in-order. That is the
nodes will be walked in the order of left->root->right
until the tree has been full traversed.
"""
def inorder_trav(root):

    # empty stack is created
    stack = deque()
    
    # set starting point to the root of the tree
    current = root

    # while the tree still has nodes, loop
    while True:

        # if there is a node, put in on the stack and
        # move left
        if current is not None:
            stack.append(current)
            current = current.left

        # else, get the last element from the stack and
        # peint it, then move to the right of it - only if
        # stack is not empty
        elif stack:
            current = stack.pop()
            print(current.data, end='->') # arrow pointing to next walk node
            current = current.right
            # after this step, the in-order walk for
            # one node is complete, and it loops for the
            # next node

        # if stack is empty, break the loop
        else:
            break



"""
Main function to test the tree walk algorithm. Tree walk test:

      1
     / \
    6   9
   / \ / \
  2  7 5  10
    
"""
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(6)
    root.right = Node(9)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(10)
    root.right.left = Node(5)
    inorder_trav(root)
