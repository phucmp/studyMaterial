# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # Assumptions:
        # 1. No duplicates will occur in BST, meaning that it will be unique
        # 2. BST will be balanced
        # 3. TreeNode already have structure of Tree
        start = root
        node = TreeNode(val)
        isLeft = False
        while root is not None:
            prev = root
            if val < root.val:
                root = root.left
                isLeft = True
            else:
                root = root.right
                isLeft = False
        if (isLeft):
            prev.left = node
        else:
            prev.right = node
        return start