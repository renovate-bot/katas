import pytest

from kata.leetcode.binary_tree_preorder_traversal import Solution
from kata.leetcode.common import Tree


class TestTreePreorderTraversal:
    @pytest.mark.parametrize('hierarchical_traversal_list, result', [
        ([1, None, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, 2])
    ])
    def test_cases(self, hierarchical_traversal_list, result):
        root = Tree(vals=hierarchical_traversal_list).root
        assert Solution().preorderTraversal(root) == result
