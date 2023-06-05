# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if(root == None):
            return res 
        queue = []
        curr = [root]
        while curr:
            level = []
            values = []
            for node in curr:
                values.append(node.val)
                if(node.left != None):
                   level.append(node.left)
                if(node.right != None):
                   level.append(node.right)
            curr = level
            res.append(values)
        return res
