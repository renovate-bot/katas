from typing import Optional, List

from kata.leetcode.common import TreeNode


class Solution:
    # recursion
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    # iteration

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result, temp = [], [root]

        while temp:
            node = temp.pop()
            result.append(node.val)

            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        return result
