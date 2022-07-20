import pytest

from kata.leetcode.add_binary import Solution


@pytest.mark.parametrize('l1, l2, result', [
    ["11", "1", "100"],
    ["1010", "1011", "10101"],
    ["0", "0", "0"],
    ["1111", "1111", "11110"]
])
def test_case(l1, l2, result):
    assert Solution().addBinary(l1, l2) == result
