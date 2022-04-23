from kata.leetcode.compare_string_with_backspace import Solution


class TestCompareString:

    def test_should_return_true_when_given_happy_case_1(self):
        s = "ab#c"
        t = "ad#c"
        assert Solution().backspaceCompare(s, t) is True

    def test_should_return_true_when_given_happy_case_2(self):
        s = "ab##"
        t = "c#d#"
        assert Solution().backspaceCompare(s, t) is True

    def test_should_return_true_when_given_happy_case_3(self):
        s = "a##c"
        t = "#a#c"
        assert Solution().backspaceCompare(s, t) is True

    def test_should_return_true_when_given_invalid_case_1(self):
        s = "a#c"
        t = "b"
        assert Solution().backspaceCompare(s, t) is False
