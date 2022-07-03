from typing import Optional, List

from kata.leetcode.common import TreeNode


class Solution:

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result, node, stack = [], root, []

        if not root:
            return []

        while node or stack:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result
