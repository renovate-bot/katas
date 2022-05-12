from kata.leetcode.binary_gap import Solution


class TestBinaryGap:

    def test_case_1(self):
        assert Solution().binary_gap(5) == 2

    def test_case_2(self):
        assert Solution().binary_gap(22) == 2

    def test_case_3(self):
        assert Solution().binary_gap(8) == 0
