# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        # def helper(root):
        def dfs(node):
            if node is None:
                return 0 
            
            total = 0 
            
            # check if the left child is a leaf 
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val # add the val of child node to the total 
            
            # recurse on both sides 
            total += dfs(node.left)
            total += dfs(node.right)
            
            # after dfs return total 
            return total 
        
        return dfs(root)

        