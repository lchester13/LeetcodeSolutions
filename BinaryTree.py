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
    
    # 104. Maximum Depth of Binary Tree

    def maxDepth(self, root):
        """
        Given the root of a binary tree, return its maximum depth.
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        def dfs(root, depth):
            if not root: 
                return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth+1))
        return dfs(root, 0)
    
    # 108. Convert Sorted Array to Binary Search Tree

    def sortedArrayToBST(self, nums):
        """
        Given an integer array nums where the elements are sorted in ascending order, 
        convert it to a height-balanced binary search tree
        """
        if not nums:
            return None
        def sort(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = sort(left, mid-1)
            root.right = sort(mid+1, right)
            return root
        return sort(0, len(nums)-1)

    # 226. Invert Binary Tree

    def invertTree(self, root):
        """
        Given the root of a binary tree, invert the tree, and return its root.
        """
        if not root:
            return None
        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    # 543. Diameter of Binary Tree
    # def diameterOfBinaryTree(self, root):

