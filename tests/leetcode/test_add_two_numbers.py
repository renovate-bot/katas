import pytest

from kata.leetcode.add_two_number import Solution
from kata.leetcode.common import LinkedList


@pytest.mark.parametrize('l1, l2, result', [
    [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
    [[0], [0], [0]],
    [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]]
])
def test_case(l1, l2, result):
    left = LinkedList()
    left.init_list(data=l1)

    right = LinkedList()
    right.init_list(data=l2)

    actual = LinkedList()
    actual.head = Solution().addTwoNumbers(left.head, right.head)
    assert actual.push_in_list() == result
