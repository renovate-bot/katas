from typing import Optional, List

from kata.leetcode.common import TreeNode


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        print("-------")
        print(root.val)
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
