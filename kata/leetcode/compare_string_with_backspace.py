class Solution:
    def backspaceCompare(self, s, t):
        stack_for_s = []
        stack_for_t = []

        for i in s:
            if i != "#":
                stack_for_s.append(i)
            else:
                if stack_for_s:
                    stack_for_s.pop()

        for j in t:
            if j != "#":
                stack_for_t.append(j)
            else:
                if stack_for_t:
                    stack_for_t.pop()

        return stack_for_s == stack_for_t
