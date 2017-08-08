# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Y2017.TreeNode import TreeNode


class Solution(object):
    #TLEed. Passed 211/212 test cases.
    #A naive method that wasted the feature of BST.
    def convertBST(self, root):
        list=[]
        self.getAllNode(root,list)
        list=sorted(list,reverse=True)
        self.convertTree(root,list)
        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

    def getAllNode(self,root,list):
        if root:
            list.append(root.val)
            self.getAllNode(root.left,list)
            self.getAllNode(root.right,list)

    def convertTree(self,root,list):
        if root:
            val=root.val
            for num in list:
                if num>val:
                    root.val+=num
                if num<=val:
                    break
            self.convertTree(root.left, list)
            self.convertTree(root.right, list)


t1=TreeNode(5)
t2=TreeNode(2)
t3=TreeNode(13)
t1.left=t2
t1.right=t3
obj=Solution()
print(obj.convertBST(t1))