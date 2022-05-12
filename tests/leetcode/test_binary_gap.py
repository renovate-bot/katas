from kata.leetcode.binary_gap import Solution


class TestBinaryGap:

    def test_case_1(self):
        assert Solution().binaryGap(5) == 2

    def test_case_2(self):
        assert Solution().binaryGap(22) == 2

    def test_case_3(self):
        assert Solution().binaryGap(8) == 0

    def test_case_4(self):
        assert Solution().binaryGap(6) == 1
