from typing import Optional, List

from kata.leetcode.common import TreeNode


class Solution:
    # recursion
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    # iteration
