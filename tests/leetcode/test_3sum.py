from kata.leetcode.three_sum import Solution


class TestBinaryGap:
    def test_case_1(self):
        assert Solution([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
