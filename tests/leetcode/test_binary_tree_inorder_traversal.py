import pytest

from kata.leetcode.binary_tree_inorder_traversal import Solution
from kata.leetcode.common import Tree


class TestTreeInorderTraversal:
    @pytest.mark.parametrize('hierarchical_traversal_list, result', [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1], [1]),
        ([], [])
    ])
    def test_cases(self, hierarchical_traversal_list, result):
        root = Tree(vals=hierarchical_traversal_list).root
        assert Solution().inorderTraversal(root) == result



