from kata.leetcode.valid_bracket import Solution


class TestValidBracket:

    def test_should_return_true_when_given_valid_case_1(self):
        s = "()"
        assert Solution().is_valid(s) is True

    def test_should_return_true_when_given_valid_case_2(self):
        s = "()[]{}"
        assert Solution().is_valid(s) is True

    def test_should_return_true_when_given_valid_case_3(self):
        s = "{[]}"
        assert Solution().is_valid(s) is True

    def test_should_return_false_when_given_invalid_case_1(self):
        s = "(]"
        assert Solution().is_valid(s) is False

    def test_should_return_false_when_given_invalid_case_2(self):
        s = "([)]"
        assert Solution().is_valid(s) is False

    def test_should_return_false_when_given_invalid_case_3(self):
        s = "(])"
        assert Solution().is_valid(s) is False
