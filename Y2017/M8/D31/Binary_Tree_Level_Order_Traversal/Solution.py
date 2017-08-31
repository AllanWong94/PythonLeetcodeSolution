# Runtime: 45ms Beats or equals to 86% One-time AC!
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        res=[]
        self.helper(root,0,res)
        return res




    def helper(self,node,depth,res):
        if node:
            if len(res)<depth+1:
                res.append([node.val])
            else:
                res[depth].append(node.val)
            self.helper(node.left,depth+1,res)
            self.helper(node.right,depth+1,res)


