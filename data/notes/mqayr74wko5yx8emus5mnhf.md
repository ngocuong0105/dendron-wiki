
Recursive traversals are easy. You do a DFS and depending on pre, in, post order you record the node values before, between or after visiting the two children.

Iterative traversals are a bit trickier. A few principles you follow:
- use a stack (every recursive algorithm can be emulated using a stack)
- each iteration you pop the last node of the stack
- in in order and post order traversal you need to bring back the node in the stack you you haven't visited left or both children
- append to stack right and then left node to simulate DFS recursive

Why would you want to do iterative vs recursive algos? Because in Python the max Call stack is like 1000 depth (unless you explicitly increase it).

# Pre order
- [leetcode](https://leetcode.com/problems/binary-tree-preorder-traversal/)
```python
# Node Left Right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root: return
            pre.append(root.val)
            dfs(root.left)
            dfs(root.right)
        pre = []
        dfs(root)
        return pre
# opposed to post or in order you don't need to check if children were passed thorugh
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            pre.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return pre
```

# In order
-[leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal/)
```python
# Left Node Right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root: return
            dfs(root.left)
            in_order.append(root.val)
            dfs(root.right)
        in_order = []
        dfs(root)
        return in_order

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root,False)] if root else []
        in_order = []
        while stack:
            node, visited_left = stack.pop()
            if visited_left:
                in_order.append(node.val)
                if node.right: stack.append((node.right,False))
            else: # visit left if you haven't
                stack.append((node,True))
                if node.left: stack.append((node.left,False))
        return in_order
```
# Post order
-[leetcode](https://leetcode.com/problems/binary-tree-postorder-traversal/)
```python
# Left Right Node
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            post.append(root.val)
        post = []
        dfs(root)
        return post

# definition of post order is to visit children first and then visit node
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post = []
        stack = [(root,False)] if root else []
        while stack:
            node, visited_children = stack.pop()
            if visited_children:
                post.append(node.val)
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
        return post
```