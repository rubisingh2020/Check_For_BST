# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296

# A binary tree node


class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Returns true if the given tree is a binary search tree
# (efficient version)
def isBST(node):
	return (isBSTUtil(node, INT_MIN, INT_MAX))

# Returns true if the given tree is a BST and its values
# >= min and <= max


def isBSTUtil(node, mini, maxi):

	# An empty tree is BST
	if node is None:
		return True

	# False if this node violates min/max constraint
	if node.data < mini or node.data > maxi:
		return False

	# Otherwise check the subtrees recursively
	# tightening the min or max constraint
	return (isBSTUtil(node.left, mini, node.data - 1) and
			isBSTUtil(node.right, node.data+1, maxi))


# Driver code
if __name__ == "__main__":
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

# Function call
if (isBST(root)):
	print("Is BST")
else:
	print("Not a BST")
