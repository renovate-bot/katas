class Solution:

    bracket_dict = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    def is_valid(self, brackets):
        left_brackets = ["(", "[", "{"]
        right_brackets = [")", "]", "}"]
        stack = []
        if len(brackets) % 2:
            return False
        for value in brackets:
            if len(stack) == 0 and value in right_brackets:
                return False
            if value in left_brackets:
                stack.append(value)
            elif value in right_brackets and stack[-1] == self.bracket_dict.get(value):
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().is_valid("(])"))
