# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -inf
        def maxPath(root):
            if root == None:
                return 0 
            lh = max(maxPath(root.left),0)
            rh = max(maxPath(root.right),0)
            self.res = max(self.res,root.val+lh+rh)
            return root.val + max(lh,rh)
        maxPath(root)
        return self.res
