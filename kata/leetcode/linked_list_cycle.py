"""
https://leetcode.cn/problems/linked-list-cycle
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next_node = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = ListNode(0)
        start.next_node = head
        slow = start
        fast = start.next_node
        while slow != fast:
            if not fast or not fast.next_node:
                return False
            slow = slow.next_node
            fast = fast.next_node.next_node
        return True


class FirstSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        linked_list_hash = {}
        p = head
        index = 0
        while p:
            if p in linked_list_hash.values():
                return True
            linked_list_hash.update({index: p})
            p = p.next_node
            index += 1

        return False
