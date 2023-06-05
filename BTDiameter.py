# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root):
               if root == None:
                          return 0 
               lh = 1 + solve(root.left)
               rh = 1 + solve(root.right)
               res = lh + rh - 2
               self.mx = max(self.mx,res)
               return max(lh,rh)
        self.mx = 0
        solve(root)
        return self.mx
