# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if(root == None):
            return res 
        q = deque([root])
        flag = True
        while q:
            n = len(q)
            curr = [0]*n
            for i in range(n):
                node = q.popleft()
                if flag:
                    idx = i 
                else:
                    idx = n-i-1
                curr[idx] = node.val 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr)
            flag = not flag 
        return res
