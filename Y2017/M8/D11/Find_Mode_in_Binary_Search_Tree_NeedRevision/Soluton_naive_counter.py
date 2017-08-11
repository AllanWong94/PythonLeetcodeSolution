class Solution(object):
    # Runtime: 122ms Beats 22%
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        count = collections.Counter()

        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        max_ct = max(count.itervalues())
        return [k for k, v in count.iteritems() if v == max_ct]