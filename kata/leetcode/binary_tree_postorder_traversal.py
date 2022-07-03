from typing import Optional, List

from kata.leetcode.common import TreeNode


class Solution:
    # recursion
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # iteration
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack = [], []
        p = root

        while p or stack:
            while p:
                result.insert(0, p.val)
                stack.append(p)
                p = p.right

            p = stack.pop().left

        return result
