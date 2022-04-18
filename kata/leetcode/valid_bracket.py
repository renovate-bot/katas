class Solution:

    def is_valid(self, brackets):
        stack = []
        for value in brackets:
            if len(stack) == 0 and value in [")", "]", "}"]:
                return False
            if value in ["(", "[", "{"]:
                stack.append(value)
            elif value == ")" and stack[-1] == "(":
                stack.pop()
            elif value == "]" and stack[-1] == "[":
                stack.pop()
            elif value == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().is_valid("(])"))
