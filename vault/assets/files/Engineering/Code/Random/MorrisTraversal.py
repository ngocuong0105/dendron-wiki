#%%
def MorrisTraversal(root):
	'''
	In order traversal of binary tree in O(1) space!
	No recursion and no stack
	Starting from the curr = root, for each node we find immediate predecessor and
	create link(portal) from pred -> curr
	'''
	# Set current to root of binary tree
	curr = root

	while(curr is not None):

		if curr.left is None:
			print(curr.value, end='->')
			curr = curr.right
		else:
			# Find the previous (prev) of curr
			prev = curr.left
            # create portal back to curr if there is not one already
			while(prev.right is not None and prev.right != curr):
				prev = prev.right

			# Make curr as right child of its prev -> create portal
			if prev.right is None:
				prev.right = curr
				curr = curr.left
			# fix the right child of prev
			elif prev.right == curr:
				prev.right = None # destroy portal
				print(curr.value, end='->') # print the root
				curr = curr.right

# #And now for some tests. Try "pip3 install binarytree" to get the needed package which will visually
# # display random binary trees
import binarytree as b
for _ in range(10):
    print()
    print("Example #",_)
    tree=b.tree()
    print(tree)
    MorrisTraversal(tree)