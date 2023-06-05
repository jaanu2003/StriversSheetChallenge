# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    def height(self,root):
            if root == None:
                return 0 
            lt =  self.height(root.left)
            rt = self.height(root.right)
            if abs(lt-rt)>1 or lt < 0 or rt < 0:
                return -1 
            return 1 + max(lt,rt)
        
