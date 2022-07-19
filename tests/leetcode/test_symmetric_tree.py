import pytest

from kata.leetcode.symmetric_tree import Solution
from kata.leetcode.common import Tree


class TestSymmetric:
    @pytest.mark.parametrize('hierarchical_traversal_list, result', [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False)
    ])
    def test_cases(self, hierarchical_traversal_list, result):
        root = Tree(vals=hierarchical_traversal_list).root
        assert Solution().isSymmetric(root) == result
