def process_string_in_stack(s, stack_for_string):
    for i in s:
        if i != "#":
            stack_for_string.append(i)
        else:
            if stack_for_string:
                stack_for_string.pop()
    return stack_for_string


class Solution:
    def backspaceCompare(self, s, t):
        return process_string_in_stack(s, []) == process_string_in_stack(t, [])
