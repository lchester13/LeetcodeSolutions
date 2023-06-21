"""
LeetCode TreeNode class for binary tree problems
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LeetCodeSolutions:
    # 94. Binary Tree Inorder Traversal
    """
    Given the root of a binary tree, return the inorder traversal of its nodes' values.
    Recursive solution
    """
    def inorderTraversal(self, root):
             stack = []
             def traverse(root):
                if not root:
                     return
                traverse(root.left)
                stack.append(root.val)
                traverse(root.right)
             traverse(root)
             return stack

    def inorderTraversalIter(self,root):
        """
        iterative solution
        """
        stack = []
        result = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

            