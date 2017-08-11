from Y2017.TreeNode import TreeNode


# Morris Traversal!

class Solution(object):
    currVal=None
    currCount=maxCount=modeCount=0
    modes=None
    def findMode(self, root):
        self.inorder(root)
        self.modes=[None]*self.modeCount
        self.modeCount=0
        self.currCount=0
        self.inorder(root)
        return self.modes

    def handleValue(self,val):
        if val!=self.currVal:
            self.currVal=val
            self.currCount=0
        if self.currCount>self.maxCount:
            self.maxCount=self.currCount
            self.modeCount=1
        elif self.currCount==self.maxCount:
            if not self.modes:
                self.modes[self.modeCount]=self.currVal
            self.modeCount+=1

    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.handleValue(root.val)
        self.inorder(root.right)