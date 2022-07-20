"""
https://leetcode.cn/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b)) + 1
        a = f"{'0' * (length - len(a))}{a}"
        b = f"{'0' * (length - len(b))}{b}"

        a_list, b_list = list(a), list(b)
        a_list.reverse()
        b_list.reverse()

        carry_bit = 0
        result = []
        for i in range(length):
            value = int(a_list[i]) + int(b_list[i]) + carry_bit

            if value > 1:
                value = value % 2
                carry_bit = 1
            else:
                carry_bit = 0
            result.append(str(value))
        if result[-1] == "0":
            result.pop()
        result.reverse()
        return "".join(result)
