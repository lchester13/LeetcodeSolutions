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
   
    def inorderTraversal(self, root):
        """
        Given the root of a binary tree, return the inorder traversal of its nodes' values.
        Recursive solution
        """
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

    # 101. Symmetric Tree

    def isSymmetric(root):
        """
        Given the root of a binary tree, check whether it is a mirror of itself 
        (i.e., symmetric around its center).
        """
        if root == None:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
            dfs(left.left, right.right) 
            and dfs(left.right, right.left))
        return dfs(root.left,root.right)