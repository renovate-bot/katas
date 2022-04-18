class Solution:

    def is_valid(self, brackets):
        stack = []
        for i in brackets:
            if i in ["(", "[", "{"]:
                stack.append(i)
            if i == ")" and stack[-1] == "(":
                stack.pop()
            if i == "]" and stack[-1] == "[":
                stack.pop()
            if i == "}" and stack[-1] == "{":
                stack.pop()

        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    print(Solution().is_valid("((())())"))
