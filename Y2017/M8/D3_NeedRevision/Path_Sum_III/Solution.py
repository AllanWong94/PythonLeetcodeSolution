class Solution(object):
    def pathSum(self, root, sum):
        self.result=0
        self.helper(root,0,sum,{0:1})
        return self.result

        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

    def helper(self, root, so_far, target, cache):
        if root:
            complement=so_far+root.val-target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val,0)
            cache[so_far+root.val] += 1
            self.helper(root.left,so_far+root.val, target, cache)
            self.helper(root.right,so_far+root.val, target, cache)
            cache[so_far+root.val] -= 1
            return

