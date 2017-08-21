# Runtime: 86ms Beats or equals to 52%


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.helper(root,None)


    def helper(self, root,next):
        if root:
            root.next=next
            self.helper(root.left,root.right)
            if next:
                self.helper(root.right,next.left)
            else:
                self.helper(root.right,None)


    # Runtime: 65ms Iterative is faster than recursive!
    # def connect(self, root):
    #     pre = None
    #     cur = root
    #     while cur:
    #         temp = cur
    #         while pre and cur:
    #             cur.next = pre.right
    #             cur = cur.next
    #             pre = pre.next
    #             if pre:
    #                 cur.next = pre.left
    #                 cur = cur.next
    #             else:
    #                 break
    #
    #         cur = temp.left
    #         pre = temp