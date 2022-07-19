from typing import Optional

from kata.leetcode.common import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.max_depth(root.left) != self.max_depth(root.right):
            return False
        left_tree = self.breadth_travel_left(root.left)
        reversed_right_tree = self.breadth_travel_right(root.right)

        print(f"left tree: {left_tree}")
        print(f"right tree: {reversed_right_tree}")
        if left_tree == reversed_right_tree:
            return True
        return False

    @staticmethod
    def max_depth(root: Optional[TreeNode]):
        if not root:
            return 0
        return max(Solution.max_depth(root.left), Solution.max_depth(root.right)) + 1

    @staticmethod
    def breadth_travel_left(root: Optional[TreeNode]):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return result

    @staticmethod
    def breadth_travel_right(root: Optional[TreeNode]):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return result
