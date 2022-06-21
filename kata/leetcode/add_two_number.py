"""
https://leetcode.cn/problems/add-two-numbers/
"""
from typing import Optional

from kata.leetcode.common import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        p = result
        carry_bit = 0
        while l1 or l2 or carry_bit:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            sum_of_two_nums = l1_value + l2_value + carry_bit
            carry_bit = sum_of_two_nums // 10

            temp = ListNode()
            temp.val = sum_of_two_nums % 10
            p.next_node = temp
            p = p.next_node
            l1 = l1.next_node if l1 else None
            l2 = l2.next_node if l2 else None

        return result.next_node
