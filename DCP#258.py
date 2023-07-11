"""
This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1

    /     \

  2         3

 / \       / \

4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Creating the binary tree same as above
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

BoustrophedonOrderList = []

def BoustrophedonOrder(root):
    if root is None:
        return

    current_level = [root]  # Start with the root node
    left_to_right = True  # Flag to indicate the traversal direction

    while current_level:
        next_level = []  # Initialize an empty list for the next level

        # Traverse the nodes in the current level
        for node in current_level:
            print(node.value, end=" ")  # Print the value of the current node

            # Enqueue the left and right child nodes depending on the traversal direction
            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

        current_level = next_level[::-1]  # Reverse the list for the next level
        left_to_right = not left_to_right  # Toggle the traversal direction


# Traversing the binary tree
print("Boustrophedon order:")
BoustrophedonOrder(root)
print("\n")

