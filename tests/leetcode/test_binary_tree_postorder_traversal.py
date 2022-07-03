import pytest

from kata.leetcode.binary_tree_postorder_traversal import Solution
from kata.leetcode.common import Tree


class TestTreePostorderTraversal:
    @pytest.mark.parametrize('hierarchical_traversal_list, result', [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1], [1]),
        ([], [])
    ])
    def test_cases(self, hierarchical_traversal_list, result):
        root = Tree(vals=hierarchical_traversal_list).root
        assert Solution().postorderTraversal(root) == result
