from kata.leetcode.two_numbers import Solution


class TestTwoNumbers:

    def test_case_1(self):
        assert Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]

    def test_case_2(self):
        assert Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2]

    def test_case_3(self):
        assert Solution().twoSum(nums=[3, 3], target=6) == [0, 1]
