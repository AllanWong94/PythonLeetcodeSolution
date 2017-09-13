# Runtime: 82ms Beats or equals to 75%
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count,k)
        return count[-1]

    def helper(self, node, count,k):
        if not node or len(count)==k:
            return

        self.helper(node.left, count,k)
        if len(count)<k:
            count.append(node.val)
            self.helper(node.right, count,k)