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
        if not root:
            return []
        result, temp = [], [root]

        while temp:
            node = temp[0]
            del temp[0]
            result.insert(0, node.val)

            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        return result
